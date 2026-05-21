"""CLI integration tests."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cli import main
from storage import TodoStorage


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "todos.json"


def test_add_creates_one(capsys: pytest.CaptureFixture, db_path: Path) -> None:
    result = main(["add", "장보기", "--db", str(db_path)])
    assert result == 0
    captured = capsys.readouterr()
    assert "추가됨" in captured.out
    todos = TodoStorage(db_path).load()
    assert len(todos) == 1
    assert todos[0].title == "장보기"


def test_list_shows_added(capsys: pytest.CaptureFixture, db_path: Path) -> None:
    main(["add", "장보기", "--db", str(db_path)])
    result = main(["list", "--db", str(db_path)])
    assert result == 0
    captured = capsys.readouterr()
    assert "장보기" in captured.out


def test_done_marks_completed(db_path: Path) -> None:
    main(["add", "장보기", "--db", str(db_path)])
    result = main(["done", "1", "--db", str(db_path)])
    assert result == 0
    todos = TodoStorage(db_path).load()
    assert todos[0].done is True


def test_rm_removes(db_path: Path) -> None:
    main(["add", "장보기", "--db", str(db_path)])
    result = main(["rm", "1", "--db", str(db_path)])
    assert result == 0
    todos = TodoStorage(db_path).load()
    assert len(todos) == 0


def test_done_missing_id_returns_1(db_path: Path) -> None:
    result = main(["done", "999", "--db", str(db_path)])
    assert result == 1
