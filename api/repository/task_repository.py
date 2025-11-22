from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .repository import Repository
from typing import List
from model.task_model import Task

class TaskRepository(Repository):
    def __init__(self, db : Session):
        super().__init__(db)

    def get_all(self) -> List[Task]: # removed optional to make code pydantic cause .all() method always return list, fullfilled or empty.
        tasks = self.db.query(Task).all()
        return tasks 

    def get_by_id(self, id: int) -> Task | None :
        return self.db.query(Task).filter(Task.id == id).first()

    def add(self, task: Task) -> Task:
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Could not add task with id and body: {task.id} -> {task}")
        return task

    def update(self, task: Task) -> Task:
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Could not update task with id: {task.id}")
        return task

    def delete(self, task: Task) -> bool:
        try:
            self.db.delete(task)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Could not delete task with id: {task.id}")
        return True
