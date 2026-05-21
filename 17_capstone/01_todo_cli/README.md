# 01_todo_cli — TODO CLI

JSON 파일에 할 일을 저장·관리하는 작은 CLI. Phase 1~4 의 내용을 통합한 미니 프로젝트.

## 무엇을 보여주나
- dataclass 로 도메인 모델
- pathlib + JSON 으로 영속화
- argparse 서브커맨드 CLI
- pytest 로 단위 + 통합 테스트
- 타입 힌트
- tempfile 로 테스트 격리

## 실행
폴더 이름이 숫자로 시작해 `python -m` 형식은 못 쓰고 파일 경로 직접:

```bash
uv run python 17_capstone/01_todo_cli/src/cli.py add "장보기" --db /tmp/_todos.json
uv run python 17_capstone/01_todo_cli/src/cli.py list --db /tmp/_todos.json
uv run python 17_capstone/01_todo_cli/src/cli.py done 1 --db /tmp/_todos.json
uv run python 17_capstone/01_todo_cli/src/cli.py rm 1 --db /tmp/_todos.json
```

## 테스트

```bash
uv run pytest 17_capstone/01_todo_cli/tests/ -q
```
