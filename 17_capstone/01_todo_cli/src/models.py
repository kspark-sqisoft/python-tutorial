"""Todo domain model."""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Todo":
        return cls(
            id=d["id"],
            title=d["title"],
            done=d.get("done", False),
            created_at=d.get("created_at", datetime.now().isoformat(timespec="seconds")),
        )
