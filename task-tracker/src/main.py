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

data_handler.close()
