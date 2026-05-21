"""
모킹 — 외부 의존성을 가짜 객체로 대체해 단위 테스트를 격리한다.
unittest.mock 의 MagicMock 과 patch 를 활용하며,
호출 여부·인자·반환값을 자유롭게 제어할 수 있다.
"""

import pytest
from unittest.mock import MagicMock, patch

# ──── 1. 테스트 대상 코드 ────

def fetch_user_name(user_id: int) -> str:
    """DB 나 외부 API 에서 사용자 이름을 가져온다고 가정."""
    raise NotImplementedError("실제 구현은 외부 I/O 필요")


def greet(user_id: int) -> str:
    """사용자 이름을 가져와 인사말을 만든다."""
    name = fetch_user_name(user_id)
    return f"안녕하세요, {name}님!"


# ──── 2. MagicMock 직접 사용 ────

def test_magic_mock_basic():
    mock = MagicMock()
    # 어떤 속성이나 메서드 호출도 자동으로 받아준다
    mock.some_method(42)
    mock.some_method.assert_called_with(42)   # 호출 인자 검증
    assert mock.some_method.call_count == 1


def test_magic_mock_return_value():
    mock = MagicMock()
    mock.return_value = "테스트 값"
    result = mock()
    assert result == "테스트 값"


# ──── 3. patch 로 함수 일시 교체 ────

def test_greet_with_patch():
    # patch 의 대상은 '모듈경로.함수명' 문자열
    with patch(f"{__name__}.fetch_user_name") as mock_fetch:
        mock_fetch.return_value = "홍길동"      # 가짜 반환값 지정
        result = greet(1)
        mock_fetch.assert_called_with(1)        # 올바른 인자로 호출됐는지 검증
    assert result == "안녕하세요, 홍길동님!"


# ──── 4. 내장 함수 모킹 예시 ────

def test_patch_builtin_print():
    # builtins.print 를 가짜로 교체해 출력을 가로챈다
    with patch("builtins.print") as mock_print:
        print("hello mock")
        mock_print.assert_called_once_with("hello mock")


# ──── 5. 실행 ────

if __name__ == "__main__":
    pytest.main(["-q", __file__])
