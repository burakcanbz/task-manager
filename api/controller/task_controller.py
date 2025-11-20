from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from dto.task_schema import TaskCreate, TaskResponse, TaskUpdate
from repository.task_repository import Repository
from service.task_service import TaskService
from config.di import get_task_service, get_task_repository

router = APIRouter(prefix="", tags=["task_items"])

@router.get("/", response_model=List[TaskResponse])
def get_tasks(service: TaskService = Depends(get_task_service), repo: Repository = Depends(get_task_repository)):
    return service.get_all(repo)

@router.post("/", response_model=TaskResponse)
def add_task(task: TaskCreate, service: TaskService = Depends(get_task_service), repo: Repository = Depends(get_task_repository)):
    return service.add_task(task, repo)

@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate, service: TaskService = Depends(get_task_service), repo: Repository = Depends(get_task_repository)):
    return service.update_task(id, task, repo)

@router.delete("/{id}")
def delete_task(id: int, service: TaskService = Depends(get_task_service), repo: Repository = Depends(get_task_repository)):
    return service.delete_task(id, repo)