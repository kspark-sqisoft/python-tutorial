"""pytest 픽스처: TestClient + DB 리셋."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

# 17_capstone/02_book_api 를 sys.path 에 추가해 `from src.xxx import ...` 가능하게 함
_BASE = Path(__file__).parent.parent
if str(_BASE) not in sys.path:
    sys.path.insert(0, str(_BASE))

from src.app import app  # noqa: E402
from src.db import Base, get_session  # noqa: E402

# 테스트 전용 engine: StaticPool 로 단일 커넥션 공유 → 모든 세션이 같은 in-memory DB 사용
_TEST_ENGINE = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
_TestSession = sessionmaker(bind=_TEST_ENGINE, autoflush=False, autocommit=False)


def _override_get_session():
    """앱의 get_session 을 테스트 DB 세션으로 대체."""
    s = _TestSession()
    try:
        yield s
    finally:
        s.close()


@pytest.fixture
def client() -> TestClient:
    """각 테스트마다 DB 를 초기화하고 TestClient 반환."""
    Base.metadata.drop_all(_TEST_ENGINE)
    Base.metadata.create_all(_TEST_ENGINE)
    app.dependency_overrides[get_session] = _override_get_session
    yield TestClient(app)
    app.dependency_overrides.clear()
