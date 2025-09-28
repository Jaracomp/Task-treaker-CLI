from functools import wraps
from dataclasses import dataclass, field
from argparse import ArgumentParser
from typing import Any, List, Dict, Callable, Optional
from types import FunctionType


@dataclass
class CommandMeta:
    name: str
    help: str
    func: Callable[..., Any]
    args: List[Dict[str, Any]] = field(default_factory=list)
    epilog: Optional[str] = None


class CLIApp:
    def __init__(self, prog: str = "task-cli", description: str = "Task tracker CLI"):
        self.prog = prog
        self.description = description
        self.commands: List[CommandMeta] = []

    def command(
        self,
        name: Optional[str] = None,
        help: Optional[str] = None,
        args: List[Dict[str, Any]] = [],
        epilog: Optional[str] = None,
    ):
        def decorator(func: FunctionType):
            command_name: str = name or func.__name__.replace("_", "-")
            command_help: Optional[str] = help or func.__doc__ or ""

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            self.commands.append(
                CommandMeta(
                    name=command_name,
                    help=command_help,
                    func=wrapper,
                    args=args,
                    epilog=epilog,
                )
            )
            return wrapper

        return decorator

    def run(self) -> None:
        parser = ArgumentParser(prog=self.prog, description=self.description)
        subparsers = parser.add_subparsers(dest="command", required=True)

        for cmd in self.commands:
            subparser = subparsers.add_parser(
                name=cmd.name, help=cmd.help, epilog=cmd.epilog
            )
            for arg in cmd.args:
                subparser.add_argument(**arg)
            subparser.set_defaults(func=cmd.func)

        args = parser.parse_args()
        args.func(args)

    def __call__(self) -> None:
        self.run()
