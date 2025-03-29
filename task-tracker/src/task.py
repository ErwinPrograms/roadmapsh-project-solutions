from datetime import datetime
from enum import Enum, auto


class TaskStatus(Enum):
    DONE = auto()
    IN_PROGRESS = auto()
    TODO = auto()


class Task:
    def __init__(
        self,
        id: int,
        description: str,
        status: TaskStatus,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id: int = id
        self.description: str = description
        self.status: TaskStatus = status
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __str__(self) -> str:
        return f"ID: {self.id}, Description: {self.description}, status: {self.status}, Created At: {self.created_at}, Last Update: {self.updated_at}"
    
    def mark_done(self) -> None:
        self.status = TaskStatus.DONE
        self.updated_at = datetime.now()
    
    def mark_in_progress(self) -> None:
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now()
