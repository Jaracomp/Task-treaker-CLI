from argparse import ArgumentParser
from src.commands import COMMANDS


def main():
    parser = ArgumentParser(prog="task-cli", description="Task tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subparsers for each command and their arguments
    for cmd in COMMANDS:
        subparser = subparsers.add_parser(
            name=cmd["name"], help=cmd["help"], epilog=cmd.get("epilog", None)
        )
        for arg in cmd["args"]:
            subparser.add_argument(**arg)
        subparser.set_defaults(func=cmd["func"])

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
