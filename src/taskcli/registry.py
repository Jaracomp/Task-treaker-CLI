from functools import wraps
from typing import Any, Callable, List, Dict


COMMANDS: List[Dict[str, Any]] = []


def command(
    name: str, help: str, args: List[Dict[str, Any]] = [], epilog: str | None = None
):
    def decorator(func: Callable):
        @wraps(func)  # Сохраняет имя/док функции
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        COMMANDS.append(
            {
                "name": name,
                "help": help,
                "func": func,
                "args": args,
                "epilog": epilog,
            }
        )
        return wrapper

    return decorator
