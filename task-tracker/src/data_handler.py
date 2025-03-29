# Time zones are outside the scope of this project
from datetime import datetime
from task import Task, TaskStatus
import json_access

STORAGE_PATH: str = "tasks.json"


def load_tasks(path: str) -> dict[int, Task]:
    tasks: list[Task] = json_access.read_tasks(path)

    if not tasks:
        return

    for task in tasks:
        id_tasks[task.id] = task


def save_tasks(path: str) -> None:
    json_access.write_tasks(path, list(id_tasks.values()))


def open() -> None:
    id_tasks = load_tasks(STORAGE_PATH)


def close() -> None:
    save_tasks(STORAGE_PATH)


def get_next_available_id() -> int:
    ids: list[int] = list(id_tasks.keys())

    if len(ids) == 0:
        return 1

    return max(ids) + 1


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


def list_tasks() -> str:
    tasks: list[Task] = list(id_tasks.values())
    result: str = ""

    # English grammar is different depending on plurality
    if len(tasks) == 1:
        result += f"There is {len(tasks)} task\n"
    else:
        result += f"There are {len(tasks)} tasks\n"

    for task in tasks:
        result += str(task) + '\n'

    return result


id_tasks: dict[int, Task] = {}
