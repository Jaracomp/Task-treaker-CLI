from .task_cli_functions import (
    list_tasks,
    add_task,
    delete_task,
    update_task,
    mark_to_do,
    mark_in_progress,
    mark_done,
)
from typing import Dict, List, Union, Callable, Any

COMMANDS: List[Dict[str, Any]] = [
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
