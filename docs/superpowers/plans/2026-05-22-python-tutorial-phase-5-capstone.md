# Python Tutorial — Phase 5 (Capstone 미니 프로젝트) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development.

**Goal:** Phase 1~4 에서 배운 내용을 통합한 미니 프로젝트 2개를 `17_capstone/` 안에 만든다. 각 프로젝트는 독립 실행·테스트 가능.

**Architecture:** `17_capstone/01_todo_cli/` (스탠드얼론 CLI) + `17_capstone/02_book_api/` (FastAPI 마이크로 서비스). 각 폴더는 `src/` + `tests/` + `README.md`. 한 서브에이전트가 한 프로젝트씩 작업.

**Tech Stack:** Python 3.12, pydantic, pytest, FastAPI(TestClient), SQLAlchemy(in-memory), argparse(stdlib), pathlib, tempfile.

**참조:** Phase 0~4 완료.

---

## 스타일 규칙

- 학습 자료가 아닌 "프로젝트"이므로 형식이 조금 다르다:
  - 각 모듈은 짧은 docstring (개념 강의 X, 모듈 목적 1~2줄).
  - 일반 프로덕션 스타일 주석 (학습용 줄단위 주석 대신 의도 설명만).
  - 타입 힌트 적극 사용.
  - 함수는 작게, 파일은 단일 책임.
  - 테스트는 pytest 컨벤션 `tests/test_*.py`.
- 각 프로젝트 루트에 `README.md`: 무엇/왜/어떻게 실행/어떻게 테스트.

---

## Task 1: `17_capstone/01_todo_cli/` — TODO CLI

### 컨셉
JSON 파일에 할 일을 저장·조회·완료·삭제하는 CLI. argparse 로 인터페이스, pathlib 으로 저장 경로, dataclass 로 모델, pytest 로 테스트.

### 파일 구조

```
17_capstone/01_todo_cli/
├─ README.md
├─ src/
│   ├─ __init__.py
│   ├─ models.py        # Todo dataclass (id, title, done, created_at)
│   ├─ storage.py       # JSON 저장/로드 (tempfile 호환)
│   └─ cli.py           # argparse + 명령들 (add/list/done/rm)
└─ tests/
    ├─ test_storage.py  # storage 단위 테스트 (tempfile)
    └─ test_cli.py      # cli 통합 테스트 (sys.argv 모킹)
```

### 사양

**`models.py`** — Todo 모델
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Todo:
    id: int
    title: str
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
```
(필드 추가 시 검증 헬퍼 1~2개 — 예: `Todo.from_dict(d)`, `Todo.to_dict()`)

**`storage.py`** — JSON 저장
- `class TodoStorage:` `__init__(self, path: Path)`
- `load() -> list[Todo]` — 파일 없으면 빈 리스트
- `save(todos: list[Todo]) -> None` — JSON dump
- 모든 IO 는 UTF-8, ensure_ascii=False

**`cli.py`** — CLI
- `def build_parser() -> argparse.ArgumentParser:` 서브커맨드: add/list/done/rm
- `def main(argv: list[str] | None = None) -> int:` (테스트하기 쉽게 argv 받음)
- 저장 경로: `--db` 옵션, 기본은 `~/.todo_cli/todos.json` (테스트에선 tempfile 경로 주입)
- 각 명령 함수는 `storage` 객체와 args 만 받음 (테스트 가능하게)

### Tests

**`test_storage.py`** — 4~5개 테스트
- 빈 파일/없는 파일 로드 → 빈 리스트
- 저장 → 다시 로드 → 동일성
- 한글 제목 저장/로드

**`test_cli.py`** — 4~5개 테스트
- `main(["add", "할 일 1", "--db", tmp])` → 종료코드 0, 파일에 1건
- `main(["list", "--db", tmp])` → stdout 에 "할 일 1" 포함
- `main(["done", "1", "--db", tmp])` → done=True
- `main(["rm", "1", "--db", tmp])` → 빈 리스트
- capsys 픽스처로 stdout 캡처

### README

```markdown
# 01_todo_cli — TODO CLI

JSON 파일에 할 일을 저장·관리하는 작은 CLI. Phase 1~4 의 내용을 모아 만든 통합 프로젝트.

## 무엇을 보여주나
- dataclass 로 도메인 모델
- pathlib + JSON 으로 영속화
- argparse 서브커맨드 CLI
- pytest 로 단위 + 통합 테스트
- 타입 힌트
- tempfile 로 테스트 격리

## 실행
[bash fence]
uv run python -m 17_capstone.01_todo_cli.src.cli add "장보기"
uv run python -m 17_capstone.01_todo_cli.src.cli list
uv run python -m 17_capstone.01_todo_cli.src.cli done 1
uv run python -m 17_capstone.01_todo_cli.src.cli rm 1
[/bash fence]

또는 짧게 (cli.py 가 `__main__` 진입점 포함):
[bash fence]
uv run python 17_capstone/01_todo_cli/src/cli.py add "장보기" --db /tmp/todos.json
[/bash fence]

## 테스트
[bash fence]
uv run pytest 17_capstone/01_todo_cli/tests/ -q
[/bash fence]
```

### Steps

1. `mkdir -p 17_capstone/01_todo_cli/src 17_capstone/01_todo_cli/tests`
2. src/ 3개 파일 + `__init__.py` 작성
3. tests/ 2개 파일 작성
4. README 작성
5. CLI 직접 실행 검증:
   ```
   uv run python 17_capstone/01_todo_cli/src/cli.py add "장보기" --db /tmp/_capstone_todo.json
   uv run python 17_capstone/01_todo_cli/src/cli.py list --db /tmp/_capstone_todo.json
   rm -f /tmp/_capstone_todo.json
   ```
6. pytest 통과:
   ```
   uv run pytest 17_capstone/01_todo_cli/tests/ -q
   ```
7. 커밋:
   ```
   git add 17_capstone/01_todo_cli/
   git commit -m "feat(17_capstone/01_todo_cli): JSON 저장 CLI todo 매니저 — dataclass+argparse+pytest"
   ```

---

## Task 2: `17_capstone/02_book_api/` — Mini Book API

### 컨셉
책 CRUD 가능한 마이크로 FastAPI 서비스. SQLAlchemy in-memory DB, pydantic 모델, TestClient 로 통합 테스트.

### 파일 구조

```
17_capstone/02_book_api/
├─ README.md
├─ src/
│   ├─ __init__.py
│   ├─ db.py            # SQLAlchemy engine + Session factory
│   ├─ models.py        # SQLAlchemy ORM 모델 (Book)
│   ├─ schemas.py       # pydantic BaseModel (BookIn / BookOut)
│   └─ app.py           # FastAPI 라우트 (GET / POST / DELETE)
└─ tests/
    └─ test_app.py      # TestClient 통합 테스트
```

### 사양

**`db.py`**
- `engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})`
- `SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)`
- `Base.metadata.create_all(engine)` 은 app 시작 시 호출
- `def get_session():` — yield 의존성

**`models.py`** — ORM
```python
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    pages: Mapped[int]
```

**`schemas.py`** — pydantic
- `class BookIn(BaseModel): title: str; pages: int = Field(ge=1)`
- `class BookOut(BookIn): id: int; model_config = {"from_attributes": True}`

**`app.py`** — FastAPI
- `app = FastAPI(title="Book API")`
- `@app.on_event("startup")` 또는 `lifespan` 으로 `Base.metadata.create_all(engine)` (lifespan 권장)
- 라우트:
  - `GET /books` → 모든 책 list
  - `POST /books` → 생성 (BookIn) → BookOut
  - `GET /books/{book_id}` → 단일 (404 가능)
  - `DELETE /books/{book_id}` → 204
- 의존성: `Depends(get_session)`

### Tests

**`test_app.py`** — TestClient
- fixture `client` — TestClient(app)
- 각 테스트 전후로 in-memory DB 리셋 (테이블 drop+create, 또는 sessionscope 분리)
- 테스트:
  - POST /books 로 생성 → 200/201
  - GET /books → 1건 확인
  - GET /books/{id} → 같은 데이터
  - DELETE → 204, 이후 GET 404
  - 잘못된 입력(pages=0) → 422

### README

```markdown
# 02_book_api — Mini Book API

작은 책 CRUD FastAPI 서비스. Phase 4 의 FastAPI + pydantic + SQLAlchemy 를 in-memory 로 통합한 프로젝트.

## 무엇을 보여주나
- FastAPI 라우트 + 의존성 주입
- pydantic 입출력 스키마
- SQLAlchemy 2.x in-memory DB
- pytest + TestClient 통합 테스트
- lifespan 으로 DB 초기화

## 실행 (개발 서버)
[bash fence]
uv run uvicorn 17_capstone.02_book_api.src.app:app --reload
[/bash fence]
브라우저로 http://localhost:8000/docs 에서 OpenAPI UI 확인 가능.

## 테스트
[bash fence]
uv run pytest 17_capstone/02_book_api/tests/ -q
[/bash fence]
```

### Steps

1. `mkdir -p 17_capstone/02_book_api/src 17_capstone/02_book_api/tests`
2. src/ 4개 + __init__.py 작성
3. tests/ 1개 작성
4. README 작성
5. pytest 통과:
   ```
   uv run pytest 17_capstone/02_book_api/tests/ -q
   ```
6. (참고) 서버 직접 실행은 학습자 수동 — 검증 X.
7. 커밋:
   ```
   git add 17_capstone/02_book_api/
   git commit -m "feat(17_capstone/02_book_api): FastAPI + SQLAlchemy in-memory CRUD — TestClient 통합 테스트"
   ```

---

## Task 3: `17_capstone/` 루트 README

Phase 0 에서 만든 placeholder 를 실제 capstone 안내로 교체.

```markdown
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
[bash fence]
uv run pytest 17_capstone/ -q
[/bash fence]
```

### Steps
1. README 교체
2. 통합 테스트:
   ```
   uv run pytest 17_capstone/ -q
   ```
3. 커밋:
   ```
   git add 17_capstone/README.md
   git commit -m "docs(17_capstone): 루트 README — 두 capstone 프로젝트 안내"
   ```

---

## 종합 검증 (모든 Task 후)

```bash
uv run pytest 17_capstone/ -q
```
모두 통과해야 한다.

---

## 끝

Phase 5 까지 완료되면 학습 저장소가 완성된다. 이후 학습자는 폴더 번호 순서대로 학습을 진행할 수 있다.
