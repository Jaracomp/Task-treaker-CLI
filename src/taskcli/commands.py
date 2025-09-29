from datetime import datetime
from tabulate import tabulate
from .storage import load_storage, save_storage
from .registry import CLIApp
from .models import Task, TaskStatus
from typing import Any, List
from .registry import ArgMeta


app = CLIApp()


@app.command(
    name="list",
    args=[
        ArgMeta(
            dest="status",
            type=str,
            choices=TaskStatus.__args__,
            nargs="?",
            default="all",
            help="Filter by status",
        ),
    ],
    epilog="Example: task-cli list done",
)
def list_tasks(args):
    """List tasks"""

    tasks: List[dict[str, Any]] = load_storage()

    if args.status and args.status != "all":
        tasks: List[dict[str, Any]] = list(
            filter(lambda task: task["status"] == args.status, tasks)
        )

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


@app.command(
    name="add",
    args=[ArgMeta(dest="description", type=str, help="Task description")],
    epilog="Example: task-cli add '...'",
)
def add_tasks(args):
    """Add new task"""

    tasks = load_storage()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = Task(id=new_id, description=args.description).to_dict()
    tasks.append(new_task)
    save_storage(tasks)
    print(f"Task {new_id} - '{args.description}' added.")


@app.command(
    name="delete",
    args=[ArgMeta(dest="id", type=int, help="Task ID")],
    epilog="Example: task-cli delete 1",
)
def delete_tasks(args):
    """Delete task"""

    tasks = load_storage()
    for task in tasks:
        if task["id"] == args.id:
            tasks.remove(task)
            save_storage(tasks)
            print(f"Task {args.id} - '{task['description']}' deleted.")
            break
    else:
        print(f"Task {args.id} not found.")


@app.command(
    name="update",
    args=[
        ArgMeta(dest="id", type=int, help="Task ID"),
        ArgMeta(dest="new_title", type=str, help="New title"),
    ],
    epilog="Example: task-cli update 1 '...'",
)
def update_tasks(args):
    """Update task description"""

    tasks = load_storage()
    for task in tasks:
        if task["id"] == args.id:
            task["description"] = args.new_title
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_storage(tasks)
            print(f"Task {args.id} - '{args.new_title}' updated.")
            break
    else:
        print(f"Task {args.id} not found.")


@app.command(
    name="mark",
    args=[
        ArgMeta(dest="id", type=int, help="Task ID"),
        ArgMeta(
            dest="status",
            type=str,
            choices=TaskStatus.__args__,
            help="New status",
        ),
    ],
    epilog="Example: task-cli mark 1 done",
)
def mark_tasks(args):
    """Mark task status as todo, in-progress, or done"""

    tasks = load_storage()
    status = args.status
    for task in tasks:
        if task["id"] == args.id:
            task["status"] = status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_storage(tasks)
            print(f"Task {args.id} marked as {status.replace('_', ' ')}.")
            return
    print(f"Task {args.id} not found.")
