
from sqlalchemy.exc import IntegrityError
from model.task_model import Task
from dto.task_schema import TaskCreate, TaskUpdate
from typing import List

from repository.repository import Repository

class TaskService():

    def get_all(self, repository: Repository) -> List[Task]:
        return repository.get_all()
    
    "We pass new db for every request but we use same service for all requests, using coroutine here."
    def add_task(self, task_data: TaskCreate, repository: Repository) -> Task:
        return repository.add(task_data)
    
    def update_task(self, id: int, task_data: TaskUpdate, repository: Repository) -> Task:
        return repository.update(id, task_data)
    
    def delete_task(self, id: int, repository: Repository) -> str:
        return repository.delete(id)