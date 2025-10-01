from dataclasses import dataclass, field
from argparse import ArgumentParser
from typing import Any, List, Callable, Optional


@dataclass
class ArgMeta:
    dest: str
    type: Optional[type] = None
    help: Optional[str] = None
    choices: Optional[List[Any]] = None
    nargs: Optional[str] = None
    default: Optional[Any] = None


@dataclass
class CommandMeta:
    name: str
    help: str
    func: Callable
    args: List[ArgMeta] = field(default_factory=list)
    epilog: Optional[str] = None


class CLIApp:
    def __init__(self, prog: str = "task-cli", description: str = "Task tracker CLI"):
        self.prog = prog
        self.description = description
        self.commands: List[CommandMeta] = []

    def argument(self, **kwargs: Any) -> Callable:
        def decorator(func: Callable) -> Callable:
            args_list = getattr(func, "_args", [])
            args_list.append(ArgMeta(dest=kwargs.pop("dest"), **kwargs))
            setattr(func, "_args", args_list)
            return func

        return decorator

    def command(
        self,
        name: str,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            nonlocal name, help
            name = name.replace("_", "-")
            help = help or func.__doc__ or ""
            args_list: List[ArgMeta] = getattr(func, "_args", [])
            self.commands.append(
                CommandMeta(
                    name=name,
                    help=help,
                    func=func,
                    args=args_list,
                    epilog=epilog,
                )
            )
            return func

        return decorator

    def __call__(self) -> None:
        parser = ArgumentParser(prog=self.prog, description=self.description)
        subparsers = parser.add_subparsers(dest="command", required=True)

        for cmd in self.commands:
            subparser = subparsers.add_parser(
                name=cmd.name, help=cmd.help, epilog=cmd.epilog
            )
            for arg in cmd.args:
                subparser.add_argument(
                    arg.dest,
                    type=arg.type,
                    help=arg.help,
                    choices=arg.choices,
                    nargs=arg.nargs,
                    default=arg.default,
                )
            subparser.set_defaults(func=cmd.func)

        args = parser.parse_args()
        args.func(args)
