from typing import List
from datetime import datetime

from exception.exception_handler import AppException
from sqlalchemy.exc import IntegrityError
from dto.task_schema import TaskCreate, TaskUpdate, TaskResponse
from repository.repository import Repository
from model.task_model import Task
from config.logger import logger
from utils.utils import (
    set_data_to_redis,
    get_data_from_redis,
    delete_from_redis,
    add_to_redis,
    update_to_redis,
)
from utils.constants import redis_all_task_key


class TaskService:

    def __init__(self, repo: Repository):
        self.repository = repo

    async def get_all(self) -> List[Task]:
        cached_data = await get_data_from_redis(redis_all_task_key)
        if cached_data:
            await logger.info("tasks returned from cache")
            tasks_response = [TaskResponse.model_validate(t) for t in cached_data]
            return tasks_response

        tasks: List[Task] = await self.repository.get_all()
        if tasks:
            serialized = [
                TaskResponse.model_validate(task).model_dump(mode="json")
                for task in tasks
            ]
            await set_data_to_redis(
                key=redis_all_task_key, data=serialized, ttl=60 * 60
            )
        await logger.info("tasks returned from db")
        return tasks

    async def add_task(self, task_data: TaskCreate) -> Task:

        task = Task(**task_data.dict())
        try:
            saved_task = await self.repository.add(task)

            await add_to_redis(saved_task)
            await logger.info(f"Task created: {saved_task.id}")
            return TaskResponse.model_validate(saved_task)

        except IntegrityError:
            await logger.warning(f"Duplicate title: {task_data.title}")
            raise AppException(
                status_code=400,
                detail=f"Task with title: '{task_data.title}' already exists",
                code="Duplicate Title",
            )

    async def update_task(self, id: int, task_data: TaskUpdate) -> Task:
        task: Task = await self.repository.get_by_id(
            id
        )  # also redis can be apply here to get most frequent finding task.

        if not task:
            raise AppException(
                status_code=404,
                detail=f"Task with update id: '{id}' not found",
                code="Task Not Found",
            )
        update_data = task_data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        task.updatedAt = datetime.utcnow()
        updated_task = await self.repository.update(task)

        await update_to_redis(updated_task)
        return TaskResponse.model_validate(updated_task)

    async def delete_task(self, id: int) -> bool:
        task: Task = await self.repository.get_by_id(id)

        if not task:
            raise AppException(
                status_code=404,
                detail=f"Task with delete id: '{id}' not found",
                code="Task Not Found",
            )

        await delete_from_redis(task.id)
        await self.repository.delete(task.id)
        return True
