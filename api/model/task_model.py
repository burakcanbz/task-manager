from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
from config.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    status = Column(String(20), nullable=True)
    priority = Column(String(50), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)