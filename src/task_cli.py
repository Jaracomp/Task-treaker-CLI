from tabulate import tabulate
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import (
    Literal,
)
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
