from argparse import ArgumentParser
from src.commands import COMMANDS


def main():
    parser = ArgumentParser(prog="task-cli", description="Task tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for cmd in COMMANDS:
        subparser = subparsers.add_parser(cmd["name"], help=cmd["help"])
        for arg in cmd["args"]:
            subparser.add_argument(arg["name"], type=arg["type"], help=arg["help"])
        subparser.set_defaults(func=cmd["func"])

    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
