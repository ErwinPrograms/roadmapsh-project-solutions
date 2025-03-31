import argparse
import data_handler

parser = argparse.ArgumentParser(
    description="A CLI task tracker with persistent data storage", prog="task-cli"
)
subparsers = parser.add_subparsers(
    title="subcommands",
    description="Valid subcommands",
    required=True,
    dest="subcommands",
)

add_parser = subparsers.add_parser("add", help="Add a new task to the list")
add_parser.add_argument(
    "descriptions",
    help="Description of new task, accepts multiple tasks",
    type=str,
    nargs='+',
)

list_parser = subparsers.add_parser("list", help="List tasks")
list_parser.add_argument(
    "status",
    help="Filter list to only show tasks with argument status",
    choices=["done", "in-progress", "todo"],
    nargs='?',
)

mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument(
    "ids", help="ID(s) of tasks to mark as done", type=int, nargs='+'
)

mark_in_progress_parser = subparsers.add_parser(
    "mark-in-progress", help="Mark a task as in progress"
)
mark_in_progress_parser.add_argument(
    "ids", help="ID(s) of tasks to mark as in-progress", type=int, nargs='+'
)

update_parser = subparsers.add_parser("update", help="Update the description of a task")
update_parser.add_argument("id", type=int, help="ID of the task to be updated")
update_parser.add_argument("description", help="New description for task")

delete_parser = subparsers.add_parser("delete", help="Delete task")
delete_parser.add_argument("id", type=int, help="ID of task to delete")


args = parser.parse_args()

# Begin handling arguments
data_handler.open()

if args.subcommands == "add":
    if data_handler.add_tasks(*args.descriptions):
        if len(args.descriptions) > 1:
            print("Tasks added successfully.")
        else:
            print("Task added successfully.")

if args.subcommands == "list":
    print(data_handler.list_tasks(args.status))

if args.subcommands == "mark-done":
    update_status = data_handler.mark_done(*args.ids)

    # 0 indicates successful update
    if update_status == 0:
        print("Update successful")
    else:
        print(f"Error with task id: {update_status}")

if args.subcommands == "mark-in-progress":
    update_status = data_handler.mark_in_progress(*args.ids)

    # 0 indicates successful update
    if update_status == 0:
        print("Update successful")
    else:
        print(f"Error with task id: {update_status}")

if args.subcommands == "update":
    update_status = data_handler.update(args.id, args.description)

    if update_status == 0:
        print("Update successful")
    else:
        print("Error updating task")

if args.subcommands == "delete":
    update_status = data_handler.delete(args.id)

    if update_status == 0:
        print("Delete successful")
    else:
        print("Error deleting task")

data_handler.close()
