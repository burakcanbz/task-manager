from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from repository.task_repository import TaskRepository
from repository.repository import Repository
from service.task_service import TaskService
from config.db import get_db

async def get_task_repository(db: AsyncSession = Depends(get_db)) -> Repository:
    return TaskRepository(db)

async def get_task_service(repo: Repository = Depends(get_task_repository)) -> TaskService:
    return TaskService(repo)