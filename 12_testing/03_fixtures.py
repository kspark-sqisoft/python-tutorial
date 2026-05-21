"""
pytest 픽스처 — 테스트 전후 공통 준비/정리 코드를 분리한다.
@pytest.fixture 로 정의하고 테스트 함수 인자로 받아 사용한다.
scope 으로 픽스처 재사용 범위(function/module/session)를 제어한다.
"""

import tempfile
import os
import pytest

# ──── 1. 기본 픽스처 ────

@pytest.fixture
def sample_list() -> list[int]:
    # scope 기본값은 "function" — 각 테스트마다 새로 생성
    return [1, 2, 3, 4, 5]


# ──── 2. yield 픽스처 (setup / teardown) ────

@pytest.fixture
def temp_path():
    # yield 이전 : setup (테스트 시작 전)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    tmp.write(b"hello fixture")
    tmp.close()
    yield tmp.name          # 테스트 함수에 파일 경로 전달
    # yield 이후 : teardown (테스트 종료 후 자동 실행)
    os.unlink(tmp.name)


# ──── 3. scope 설명 ────
# @pytest.fixture(scope="function")  — 기본값, 매 테스트마다 실행
# @pytest.fixture(scope="module")    — 모듈(파일) 당 한 번
# @pytest.fixture(scope="session")   — pytest 세션 전체에서 한 번


# ──── 4. 픽스처를 사용하는 테스트 ────

def test_list_sum(sample_list: list[int]):
    # 인자 이름이 픽스처 이름과 같으면 자동 주입
    assert sum(sample_list) == 15


def test_list_length(sample_list: list[int]):
    assert len(sample_list) == 5


def test_temp_file_exists(temp_path: str):
    # yield 픽스처가 제공한 경로 검증
    assert os.path.exists(temp_path)


def test_temp_file_content(temp_path: str):
    with open(temp_path, "rb") as f:
        assert f.read() == b"hello fixture"


# ──── 5. 실행 ────

if __name__ == "__main__":
    pytest.main(["-q", __file__])
