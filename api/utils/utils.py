import asyncio
import json

from typing import Optional, TypeVar
from datetime import datetime
from sqlalchemy import text, delete
from sqlalchemy.exc import OperationalError
from sqlalchemy import select, func

from config.db import Base, get_db, engine, AsyncSessionLocal
from config.redis import REDIS_CLIENT
from config.logger import logger

from utils.constants import redis_all_task_key
from model.task_model import Task
from dto.task_schema import TaskResponse

T = TypeVar('T')

async def clean_tasks():
    async for db in get_db():
        try:
            result = await db.execute(delete(Task))
            deleted_count = result.rowcount
            await db.commit()
            print(f"✅ {deleted_count} tasks deleted from DB")
            return 
        except Exception as e:
            await db.rollback()
            print(f"❌ Error cleaning tasks: {e}")

async def seed_data():
    try:
        with open("./data/tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: tasks.json file not found!")
        return

    tasks_list = data["tasks"]
    
    async for db in get_db(): 
        try:
            total_added = 0
            
            for t in tasks_list:
                task = Task(
                    title=t["title"],
                    description=t["description"],
                    status=t["status"],
                    priority=t["priority"],
                    createdAt=datetime.fromtimestamp(t["createdAt"] / 1000),
                    updatedAt=datetime.fromtimestamp(t["createdAt"] / 1000)
                )
                db.add(task)
                total_added += 1

            if total_added > 0:
                await db.commit() 
                print(f"✅ Seeder finished successfully! Total {total_added} tasks added.")
            
            return 
            
        except Exception as e:
            await db.rollback()
            print(f"❌ Error seeding data: {e}")

async def check_database_connection():
    
    max_retries = 5
    retry_delay = 2  
    
    for attempt in range(max_retries):
        try:
            async with engine.begin() as conn:
                await conn.execute(text("SELECT 1")) 
            
            print("Database connection successful")
            return
            
        except OperationalError as e:
            if attempt < max_retries - 1:
                print(f"Database connection failed ({attempt+1}/{max_retries}), retrying in {retry_delay}s...")
                
                await asyncio.sleep(retry_delay) 
            else:
                print(f"Database connection failed after {max_retries} retries.")
                raise Exception("Database connection failed after multiple retries.")
            
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def database_seeder():
    async with AsyncSessionLocal() as db:
        stmt = select(func.count(Task.id))
        result = await db.execute(stmt)
        task_count = result.scalar_one()
        
        if task_count == 0:
            await logger.info("Database is empty. Starting data seeding...")
            await seed_data() 
        else:
            await logger.info(f"Database contains {task_count} tasks. Seeding skipped.")

async def check_redis_connection():
    try:
        ping = await REDIS_CLIENT.ping()
        await REDIS_CLIENT.delete(redis_all_task_key)
        await logger.info(f"Redis connected: {ping}")
    except Exception as e:
        await logger.info(f"Redis connection failed: {e}")

async def set_data_to_redis(key: str, data: T, ttl: Optional[int] = None ) -> bool:
    if not REDIS_CLIENT:
        return False
        
    try:
        serialized_data = json.dumps(data) 
    except TypeError as e:
        return False

    try:
        await REDIS_CLIENT.set(
            key, 
            serialized_data, 
            ex=ttl
        )
        return True
    except Exception as e:
        return False

async def get_data_from_redis(key: str) -> Optional[T]:
    if not REDIS_CLIENT:
        return None
        
    try:
        cached_data_str = await REDIS_CLIENT.get(key)
    except ConnectionError:
        return None

    if cached_data_str is None:
        return None
        
    try:
        data = json.loads(cached_data_str)
        return data

    except json.JSONDecodeError:
        return None
    except Exception:
        return None

async def add_to_redis(saved_task: T):
    cached_tasks = await get_data_from_redis(redis_all_task_key) or []
    task_json = TaskResponse.model_validate(saved_task).model_dump(mode="json")
    cached_tasks.append(task_json)
    await set_data_to_redis(redis_all_task_key, cached_tasks, ttl=3600)


async def update_to_redis(updated_task: T):
    cached_tasks = await get_data_from_redis(redis_all_task_key) or []
    task_json = TaskResponse.model_validate(updated_task).model_dump(mode="json")
    for i, t in enumerate(cached_tasks):
        if t["id"] == updated_task.id:
            cached_tasks[i] = task_json
            break
    await set_data_to_redis(redis_all_task_key, cached_tasks, ttl=3600)

async def delete_from_redis(id: int):
    try:
        cached_tasks = json.loads(await REDIS_CLIENT.get(redis_all_task_key) or "[]")
        cached_tasks = [t for t in cached_tasks if t["id"] != id]
        await REDIS_CLIENT.set(redis_all_task_key, json.dumps(cached_tasks), ex=3600)
    except:
        pass