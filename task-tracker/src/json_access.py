import os
import json
from data_handler import Task, TaskStatus
from datetime import datetime


def write_tasks(path: str, tasks: list[Task]) -> None:
    serializable_tasks = [None] * len(tasks)
    for i in range(len(serializable_tasks)):
        serializable_tasks[i] = task_to_serializable(tasks[i])

    json_object = json.dumps(serializable_tasks)

    with open(path, 'w') as outfile:
        outfile.write(json_object)


def read_tasks(path: str) -> list[Task]:
    if not os.path.exists(path):
        return None

    with open(path, 'r') as file:
        contents = file.read()
        dicts_list = json.loads(contents)

        tasks: list[Task] = [None] * len(dicts_list)
        for i in range(len(dicts_list)):
            tasks[i] = dict_to_task(dicts_list[i])

    return tasks


def task_to_serializable(task: Task) -> dict[str, any]:
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status.value,
        "created_at": datetime_to_serializable(task.created_at),
        "updated_at": datetime_to_serializable(task.updated_at),
    }


def dict_to_task(task_dict: dict[str, any]) -> Task:
    return Task(
        task_dict['id'],
        task_dict['description'],
        TaskStatus(task_dict['status']),
        dict_to_datetime(task_dict['created_at']),
        dict_to_datetime(task_dict['updated_at']),
    )


def datetime_to_serializable(datetime: datetime) -> dict[str, int]:
    # This application does not use time zone
    return {
        "year": datetime.year,
        "month": datetime.month,
        "day": datetime.day,
        "hour": datetime.hour,
        "minute": datetime.minute,
        "second": datetime.second,
        "microsecond": datetime.microsecond,
    }


def dict_to_datetime(unconverted_datetime: dict[str, int]) -> datetime:
    return datetime(
        unconverted_datetime['year'],
        unconverted_datetime['month'],
        unconverted_datetime['day'],
        unconverted_datetime['hour'],
        unconverted_datetime['minute'],
        unconverted_datetime['second'],
        unconverted_datetime['microsecond'],
    )
