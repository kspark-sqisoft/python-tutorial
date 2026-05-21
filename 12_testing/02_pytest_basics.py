"""
pytest 입문 — 표준 assert 구문 그대로 사용.
test_ 로 시작하는 함수/파일을 자동으로 수집하며,
실패 시 좌우 값을 상세히 보여줘 디버깅이 쉽다.
"""

import pytest

# ──── 1. 테스트 대상 함수 ────

def add(a: int, b: int) -> int:
    """두 수를 더한다."""
    return a + b


def reverse_string(s: str) -> str:
    """문자열을 뒤집는다."""
    return s[::-1]


# ──── 2. pytest 테스트 함수 ────
# 클래스 불필요 — 그냥 def test_xxx() 함수로 작성한다.
# 파일 이름과 함수 이름이 test_ 로 시작해야 pytest 가 자동 수집한다.

def test_add_positive():
    # 일반 assert 구문 그대로 사용 가능
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -2) == -3


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_reverse_empty():
    # 빈 문자열 경계 케이스
    assert reverse_string("") == ""


# ──── 3. pytest vs unittest 비교 ────
# unittest : self.assertEqual(a, b)  →  실패 시 "AssertionError: 5 != 6"
# pytest   : assert a == b           →  실패 시 "assert 5 == 6  where 5 = add(2, 3)"
# pytest 가 실패 메시지를 훨씬 자세하게 보여준다.


# ──── 4. 실행 ────

if __name__ == "__main__":
    # -q : 간결 출력 모드
    pytest.main(["-q", __file__])
