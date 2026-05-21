# 17_capstone — 미니 프로젝트

Phase 1~4 에서 배운 내용을 통합한 두 개의 작은 프로젝트.

## 프로젝트

### 01_todo_cli — TODO CLI
JSON 저장 기반 CLI todo 관리자.
- dataclass 모델 + pathlib 저장 + argparse CLI + pytest 테스트
- 자세히는 [01_todo_cli/README.md](01_todo_cli/README.md)

### 02_book_api — Mini Book API
FastAPI + SQLAlchemy in-memory CRUD 마이크로 서비스.
- pydantic 스키마 + SQLAlchemy ORM + FastAPI 라우트 + TestClient
- 자세히는 [02_book_api/README.md](02_book_api/README.md)

## 통합 테스트
```bash
uv run pytest 17_capstone/ -q
```

총 14개 테스트 (todo_cli 9 + book_api 5) 가 모두 통과해야 한다.
