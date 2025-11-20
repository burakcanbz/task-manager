from abc import ABC, abstractmethod
from typing import TypeVar, Any, List, Generic

from sqlalchemy.orm import Session

T = TypeVar("T")  # generic model type
C = TypeVar("C")  # generic create DTO type


class Repository(ABC, Generic[T, C]):

    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def add(self, item: C) -> None:
        pass

    @abstractmethod
    def update(self, id: int, item: Any) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass