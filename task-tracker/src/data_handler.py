# Time zones are outside the scope of this project
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


def load_tasks(source_path: str) -> dict[int, Task]:
    # placeholder
    return {}


def get_next_available_id() -> int:
    # placeholder
    return 1


def add_tasks(*descriptions: tuple[str]) -> None:
    datetime_of_creation = datetime.now()

    for description in descriptions:
        new_task: Task = Task(
            get_next_available_id(),
            description,
            TaskStatus.TODO,
            datetime_of_creation,
            datetime_of_creation,
        )
        id_tasks[new_task.id] = new_task

    return True

def list_tasks() -> None:
    pass

id_tasks: dict[int, Task] = load_tasks("placeholder.json")
