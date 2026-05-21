"""JSON-backed persistence layer for todos."""

import json
import sys
from pathlib import Path

if __package__:
    from .models import Todo
else:
    sys.path.insert(0, str(Path(__file__).parent))
    from models import Todo  # type: ignore[no-redef]


class TodoStorage:
    def __init__(self, path: Path) -> None:
        self._path = path

    def load(self) -> list[Todo]:
        if not self._path.exists() or self._path.stat().st_size == 0:
            return []
        with self._path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return [Todo.from_dict(d) for d in data]

    def save(self, todos: list[Todo]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in todos], f, indent=2, ensure_ascii=False)
