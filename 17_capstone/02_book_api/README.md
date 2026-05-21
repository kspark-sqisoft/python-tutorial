# 02_book_api — Mini Book API

작은 책 CRUD FastAPI 서비스. Phase 4 의 FastAPI + pydantic + SQLAlchemy 를 in-memory 로 통합.

## 무엇을 보여주나
- FastAPI 라우트 + 의존성 주입 (Depends)
- pydantic 입출력 스키마 분리 (BookIn / BookOut)
- SQLAlchemy 2.x Mapped + in-memory SQLite
- lifespan 으로 DB 초기화
- pytest + TestClient 통합 테스트

## 파일 구조

```
17_capstone/02_book_api/
├─ README.md
├─ src/
│   ├─ __init__.py
│   ├─ db.py            # engine + SessionLocal + Base + get_session
│   ├─ models.py        # SQLAlchemy ORM (Book)
│   ├─ schemas.py       # pydantic (BookIn / BookOut)
│   └─ app.py           # FastAPI app + 라우트
└─ tests/
    ├─ __init__.py
    ├─ conftest.py      # TestClient 픽스처 + DB 리셋
    └─ test_app.py
```

## 실행 (개발 서버)

폴더 이름이 숫자로 시작해 모듈 경로 import 가 까다롭다. 직접 파일을 가리켜 실행:

```bash
uv run python 17_capstone/02_book_api/src/app.py
```

또는 디렉터리로 들어가서 uvicorn 사용:

```bash
cd 17_capstone/02_book_api
uv run uvicorn src.app:app --reload
```

브라우저: http://127.0.0.1:8000/docs

## 테스트

```bash
uv run pytest 17_capstone/02_book_api/tests/ -q
```
