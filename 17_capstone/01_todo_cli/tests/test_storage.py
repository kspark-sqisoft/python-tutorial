"""Storage layer tests."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from models import Todo
from storage import TodoStorage


def test_load_missing_returns_empty(tmp_path: Path) -> None:
    storage = TodoStorage(tmp_path / "nonexistent.json")
    assert storage.load() == []


def test_save_then_load_roundtrip(tmp_path: Path) -> None:
    storage = TodoStorage(tmp_path / "todos.json")
    todos = [
        Todo(id=1, title="장보기", created_at="2026-01-01T00:00:00"),
        Todo(id=2, title="청소", done=True, created_at="2026-01-02T00:00:00"),
    ]
    storage.save(todos)
    loaded = storage.load()
    assert len(loaded) == 2
    assert loaded[0].id == 1
    assert loaded[0].title == "장보기"
    assert loaded[1].done is True


def test_save_creates_parent_dirs(tmp_path: Path) -> None:
    deep_path = tmp_path / "a" / "b" / "c" / "todos.json"
    storage = TodoStorage(deep_path)
    storage.save([Todo(id=1, title="test")])
    assert deep_path.exists()


def test_load_korean(tmp_path: Path) -> None:
    storage = TodoStorage(tmp_path / "todos.json")
    title = "한글 제목 테스트"
    storage.save([Todo(id=1, title=title)])
    loaded = storage.load()
    assert loaded[0].title == title
