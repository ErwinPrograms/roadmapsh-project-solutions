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


def list_tasks(status_filter=None) -> str:
    tasks: list[Task] = list(id_tasks.values())
    result: str = ""

    if status_filter:
        string_status: dict[str, TaskStatus] = {
            "done": TaskStatus.DONE,
            "in-progress": TaskStatus.IN_PROGRESS,
            "todo": TaskStatus.TODO,
        }

        target_status = string_status[status_filter]

        tasks = list(filter(lambda task: task.status == target_status, tasks))

    # English grammar is different depending on plurality
    if len(tasks) == 1:
        result += f"There is {len(tasks)} task\n"
    else:
        result += f"There are {len(tasks)} tasks\n"

    for task in tasks:
        result += str(task) + '\n'

    return result


def mark_done(*task_ids: tuple[int]) -> int:
    '''Marks all tasks corresponding to argument ids as done. If any IDs don't exist, no updates are done. If successful, returns 0'''
    existing_ids = list(id_tasks.keys())

    # Not updating any when any IDs are missing is intended
    for id in task_ids:
        if id not in existing_ids:
            return id

    for id in task_ids:
        id_tasks[id].mark_done()

    return 0


def mark_in_progress(*task_ids: tuple[int]) -> int:
    '''Marks all tasks corresponding to argument ids as done. If any IDs don't exist, no updates are done. If successful, returns 0'''
    existing_ids = list(id_tasks.keys())

    # Not updating any when any IDs are missing is intended
    for id in task_ids:
        if id not in existing_ids:
            return id

    for id in task_ids:
        id_tasks[id].mark_in_progress()

    return 0


def update(id: int, new_description: str):
    if id not in id_tasks.keys():
        return 1

    id_tasks[id].update_description(new_description)

    return 0


def delete(id: int):
    if id not in id_tasks.keys():
        return 1

    id_tasks.pop(id)

    return 0


id_tasks: dict[int, Task] = {}
