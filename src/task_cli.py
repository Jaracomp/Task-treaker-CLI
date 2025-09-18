# from dataclasses import dataclass
# from datetime import datetime
# from tabulate import tabulate
# from typing import (
#     Literal,
# )

FILE = ".\task-cli.json"

def list_tasks():
    print("Listing tasks")


def add_task(args):
    print(f"Adding: {args.title}")


def delete_task(args):
    print(f"Deleting {args.id}")


def update_task(args):
    print(f"Updating {args.id} -> {args.new_title}")
