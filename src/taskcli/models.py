from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Literal, TypeAlias


TaskStatus: TypeAlias = Literal["todo", "in-progress", "done"]

@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus = "todo"
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str = created_at

    def to_dict(self):
        return asdict(self)
