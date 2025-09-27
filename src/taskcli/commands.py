from dataclasses import asdict, dataclass
from datetime import datetime
from typing import (
    Literal,
)

from tabulate import tabulate

from .storage import load_storage, save_storage


@dataclass
class Task:
    id: int
    description: str
    status: Literal["todo", "in_progress", "done"] = "todo"
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str = created_at

    def to_dict(self):
        return asdict(self)


def list_tasks(args):
    tasks = load_storage()
    if tasks:
        headers = ["ID", "Description", "Status", "Created At", "Updated At"]
        table = tabulate(
            [
                [
                    task["id"],
                    task["description"],
                    task["status"],
                    task["created_at"],
                    task["updated_at"],
                ]
                for task in tasks
            ],
            headers=headers,
            tablefmt="grid",
        )
        print(table)
    else:
        print("No tasks found.")


def add_task(args):
    tasks = load_storage()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = Task(id=new_id, description=args.description).to_dict()
    tasks.append(new_task)
    save_storage(tasks)
    print(f"Task {new_id} - '{args.description}' added.")


def delete_task(args):
    tasks = load_storage()
    for task in tasks:
        if task["id"] == args.id:
            tasks.remove(task)
            save_storage(tasks)
            print(f"Task {args.id} - '{task['description']}' deleted.")
            break
    else:
        print(f"Task {args.id} not found.")


def update_task(args):
    tasks = load_storage()
    for task in tasks:
        if task["id"] == args.id:
            task["description"] = args.new_title
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_storage(tasks)
            print(f"Task {args.id} - '{args.new_title}' updated.")
            break
    else:
        print(f"Task '{args.new_title}' not found.")


def _update_task_status(task_id: int, new_status: str) -> None:
    tasks = load_storage()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_storage(tasks)
            print(f"Task {task_id} marked as {new_status.replace('_', ' ')}.")
            break
    else:
        print(f"Task {task_id} not found.")


def mark_to_do(args):
    _update_task_status(args.id, "todo")


def mark_in_progress(args):
    _update_task_status(args.id, "in_progress")


def mark_done(args):
    _update_task_status(args.id, "done")


COMMANDS = [
    {
        "name": "add",
        "help": "Add new task",
        "func": add_task,
        "args": [{"dest": "description", "type": str, "help": "Task description"}],
        "epilog": "Example: task-cli add '...'",
    },
    {
        "name": "list",
        "help": "List tasks",
        "func": list_tasks,
        "args": [],
        "epilog": "Example: task-cli list",
    },
    {
        "name": "delete",
        "help": "Delete task",
        "func": delete_task,
        "args": [{"dest": "id", "type": int, "help": "Task ID"}],
        "epilog": "Example: task-cli delete 1",
    },
    {
        "name": "update",
        "help": "Update task",
        "func": update_task,
        "args": [
            {"dest": "id", "type": int, "help": "Task ID"},
            {"dest": "new_title", "type": str, "help": "New title"},
        ],
        "epilog": "Example: task-cli update 1 '...'",
    },
    {
        "name": "mark-to-do",
        "help": "Mark task as todo",
        "func": mark_to_do,
        "args": [{"dest": "id", "type": int, "help": "Task ID"}],
        "epilog": "Example: task-cli mark-to-do 1",
    },
    {
        "name": "mark-in-progress",
        "help": "Mark task as in progress",
        "func": mark_in_progress,
        "args": [{"dest": "id", "type": int, "help": "Task ID"}],
        "epilog": "Example: task-cli mark-in-progress 1",
    },
    {
        "name": "mark-done",
        "help": "Mark task as done",
        "func": mark_done,
        "args": [{"dest": "id", "type": int, "help": "Task ID"}],
        "epilog": "Example: task-cli mark-done 1",
    },
]
