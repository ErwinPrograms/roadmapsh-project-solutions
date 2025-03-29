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
    print(data_handler.list_tasks())

if args.subcommands == "mark-done":
    update_status = data_handler.mark_done(*args.ids)

    # 0 indicates successful update
    if  update_status == 0:
        print("Update successful")
    else:
        print(f"Error with task id: {update_status}")

if args.subcommands == "mark-in-progress":
    update_status = data_handler.mark_in_progress(*args.ids)

    # 0 indicates successful update
    if  update_status == 0:
        print("Update successful")
    else:
        print(f"Error with task id: {update_status}")

data_handler.close()
