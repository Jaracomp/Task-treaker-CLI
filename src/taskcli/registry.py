from functools import wraps
from typing import Any, List, Dict


COMMANDS: List[Dict[str, Any]] = []


def command(
    name: str | None = None,
    help: str | None = None,
    args: List[Dict[str, Any]] = [],
    epilog: str | None = None,
):
    def decorator(func):
        command_name = name or func.__name__.replace("_", "-")
        command_help = help or func.__doc__ or ""

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        COMMANDS.append(
            {
                "name": command_name,
                "help": command_help,
                "func": wrapper,
                "args": args,
                "epilog": epilog,
            }
        )
        return wrapper

    return decorator
