from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    low="Low"
    medium="Medium"
    high="High"

class Status(str, Enum):
    completed="completed"
    incomplete="incomplete"

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=300)
    priority: str
    status: Status

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=300)
    priority: Priority | None  = None
    status: Status | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: Priority 
    status: Status
    createdAt: datetime 
    updatedAt: datetime

    model_config = {
        "from_attributes": True
    }