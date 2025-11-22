from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import List

from .repository import Repository
from model.task_model import Task

class TaskRepository(Repository):
    def __init__(self, db : Session):
        super().__init__(db)

    def get_all(self) -> List[Task]:
        tasks = self.db.query(Task).all()
        return tasks 

    def get_by_id(self, id: int) -> Task | None :
        return self.db.query(Task).filter(Task.id == id).first()

    def add(self, task: Task) -> Task:
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except SQLAlchemyError:
            self.db.rollback()
            raise
        return task

    def update(self, task: Task) -> Task:
        try:
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
        except SQLAlchemyError:
            self.db.rollback()
            raise
        return task

    def delete(self, task: Task) -> bool:
        try:
            self.db.delete(task)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise
        return True