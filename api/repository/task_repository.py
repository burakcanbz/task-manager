from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from typing import List

from .repository import Repository
from model.task_model import Task

class TaskRepository(Repository):
    def __init__(self, db : AsyncSession):
        super().__init__(db)

    async def get_all(self) -> List[Task]:
        s = select(Task)
        result = await self.db.execute(s)
        return result.scalars().all()

    async def get_by_id(self, id: int) -> Task | None :
        s = select(Task).filter(Task.id == id)
        result = await self.db.execute(s)
        return result.scalar_one_or_none()
    
    async def add(self, task: Task) -> Task:
        try:
            self.db.add(task)
            await self.db.commit()
            await  self.db.refresh(task)
        except SQLAlchemyError:
            await self.db.rollback()
            raise
        return task

    async def update(self, task: Task) -> Task:
        try:
            self.db.add(task)
            await self.db.commit()
            await self.db.refresh(task)
        except SQLAlchemyError:
            await self.db.rollback()
            raise
        return task

    async def delete(self, id) -> bool:
        try:
            await self.db.execute(delete(Task).where(Task.id == id))
            await self.db.commit()
        except SQLAlchemyError:
            await self.db.rollback()
            raise
        return True