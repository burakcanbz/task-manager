from fastapi import Depends
from sqlalchemy.orm import Session
from repository.task_repository import TaskRepository
from repository.repository import Repository
from service.task_service import TaskService
from config.db import get_db

"We can use other repositories here, cause we decide repository at run-time and each Repository should implement Repository Abstract Class"
def get_task_repository(db: Session = Depends(get_db)) -> Repository:
    return TaskRepository(db)

def get_task_service(repo: Repository = Depends(get_task_repository)) -> TaskService:
    return TaskService(repo)