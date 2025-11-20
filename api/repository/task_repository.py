from fastapi import HTTPException
from .repository import Repository
from typing import List, Optional
from dto.task_schema import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session
from model.task_model import Task
from datetime import datetime

class TaskRepository(Repository):
    def __init__(self, db : Session):
        super().__init__(db)

    def get_all(self) -> Optional[List[Task]] | None:
        tasks = self.db.query(Task).all()
        return tasks if tasks else None


    def add(self, task: TaskCreate) -> Task:
        task = Task(**task.dict())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, id: int, task_update: TaskUpdate) -> Task:
        task = self.db.query(Task).filter(Task.id == id).first()

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        update_data = task_update.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        task.updatedAt = datetime.utcnow()

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, id: int) -> str:
        task = self.db.query(Task).filter(Task.id == id).first()
        if not task:
            return False
        
        self.db.delete(task)
        self.db.commit()
        return {"message": "task deleted successfully."}