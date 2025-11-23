from abc import ABC, abstractmethod
from typing import TypeVar, Any, List, Generic

from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")  # generic model type
C = TypeVar("C")  # generic create DTO type


class Repository(ABC, Generic[T, C]):

    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod
    async def get_all(self) -> List[T]: 
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> T:
        pass

    @abstractmethod
    async def add(self, item: C) -> T:
        pass

    @abstractmethod
    async def update(self, item: C) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass