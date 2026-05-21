"""Argparse-based CLI entry point for todo management."""

import argparse
import sys
from pathlib import Path

# Support both `python cli.py` (direct) and `import src.cli` (package) execution
if __package__:
    from .models import Todo
    from .storage import TodoStorage
else:
    sys.path.insert(0, str(Path(__file__).parent))
    from models import Todo  # type: ignore[no-redef]
    from storage import TodoStorage  # type: ignore[no-redef]


def build_parser() -> argparse.ArgumentParser:
    default_db = Path.home() / ".todo_cli" / "todos.json"

    # Shared --db option inherited by every subparser
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--db", type=Path, default=default_db, metavar="PATH")

    parser = argparse.ArgumentParser(
        description="JSON-backed CLI TODO manager",
        parents=[shared],
    )

    sub = parser.add_subparsers(dest="command")
    sub.required = True

    p_add = sub.add_parser("add", help="Add a new todo", parents=[shared])
    p_add.add_argument("title")

    sub.add_parser("list", help="List all todos", parents=[shared])

    p_done = sub.add_parser("done", help="Mark todo as done", parents=[shared])
    p_done.add_argument("id", type=int)

    p_rm = sub.add_parser("rm", help="Remove a todo", parents=[shared])
    p_rm.add_argument("id", type=int)

    return parser


def cmd_add(storage: TodoStorage, args: argparse.Namespace) -> int:
    todos = storage.load()
    new_id = max((t.id for t in todos), default=0) + 1
    todo = Todo(id=new_id, title=args.title)
    todos.append(todo)
    storage.save(todos)
    print(f"추가됨: id={todo.id}, title={todo.title}")
    return 0


def cmd_list(storage: TodoStorage, args: argparse.Namespace) -> int:
    todos = storage.load()
    for t in todos:
        mark = "x" if t.done else " "
        print(f"[{mark}] {t.id} {t.title} ({t.created_at})")
    return 0


def cmd_done(storage: TodoStorage, args: argparse.Namespace) -> int:
    todos = storage.load()
    for t in todos:
        if t.id == args.id:
            t.done = True
            storage.save(todos)
            return 0
    print(f"오류: id={args.id} 를 찾을 수 없음", file=sys.stderr)
    return 1


def cmd_rm(storage: TodoStorage, args: argparse.Namespace) -> int:
    todos = storage.load()
    filtered = [t for t in todos if t.id != args.id]
    if len(filtered) == len(todos):
        print(f"오류: id={args.id} 를 찾을 수 없음", file=sys.stderr)
        return 1
    storage.save(filtered)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    storage = TodoStorage(args.db)

    dispatch = {
        "add": cmd_add,
        "list": cmd_list,
        "done": cmd_done,
        "rm": cmd_rm,
    }
    return dispatch[args.command](storage, args)


if __name__ == "__main__":
    sys.exit(main())
