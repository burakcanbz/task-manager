from fastapi import APIRouter, Depends
from typing import List

from dto.task_schema import TaskCreate, TaskResponse, TaskUpdate
from service.task_service import TaskService
from config.di import get_task_service

router = APIRouter(prefix="", tags=["task_items"])

@router.get("/", response_model=List[TaskResponse])
async def get_tasks(service: TaskService = Depends(get_task_service)):
    return await service.get_all()

@router.post("/", response_model=TaskResponse)
async def add_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return await service.add_task(task)

@router.put("/{id}", response_model=TaskResponse)
async def update_task(id: int, task: TaskUpdate, service: TaskService = Depends(get_task_service)):
    return await service.update_task(id, task)

@router.delete("/{id}")
async def delete_task(id: int, service: TaskService = Depends(get_task_service)):
    return await service.delete_task(id)