from .task_cli import list_tasks, add_task, delete_task, update_task


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
]
