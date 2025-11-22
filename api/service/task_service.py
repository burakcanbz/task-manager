
from typing import List
from datetime import datetime

from exception.exception_handler import AppException
from dto.task_schema import TaskCreate, TaskUpdate
from repository.repository import Repository
from model.task_model import Task

class TaskService():

    def __init__(self, repo: Repository):
        self.repository = repo

    def get_all(self) -> List[Task]: # already returning empty list if no task in db.
        return self.repository.get_all()
    
    def add_task(self, task_data: TaskCreate) -> Task:
        existing_task: List[Task] = self.repository.get_all()

        duplicate_task = next((t for t in existing_task if t.title == task_data.title), None)
        if duplicate_task:
            raise AppException(status_code=400, detail=f"Task with title: '{task_data.title}' already exists", code="Duplicate Title")
        
        task = Task(**task_data.dict())
        return self.repository.add(task)
    
    def update_task(self, id: int, task_data: TaskUpdate) -> Task:
        task: Task = self.repository.get_by_id(id)

        if not task:
            raise AppException(status_code=404, detail=f"Task with update id: '{id}' not found", code="Task Not Found")
        update_data = task_data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(task, key, value)

        task.updatedAt = datetime.utcnow()
        return self.repository.update(task)
    
    def delete_task(self, id: int) -> bool:
        task: Task = self.repository.get_by_id(id)

        if not task:
            raise AppException(status_code=404, detail=f"Task with delete id: '{id}' not found", code="Task Not Found")
        
        self.repository.delete(task)
        return True