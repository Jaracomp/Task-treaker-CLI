import json
import os
from pathlib import Path
from typing import Any, Dict, List

FILE: Path = Path("task-cli.json")


def load_storage() -> List[Dict[str, Any]]:
    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        save_storage([])
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_storage(tasks: List[Dict[str, Any]]) -> None:
    with FILE.open("w") as f:
        json.dump(tasks, f, indent=2)
