"""
parametrize — 같은 테스트 함수를 여러 입력값으로 반복 실행한다.
@pytest.mark.parametrize 로 입력/기대값 쌍을 나열하면
pytest 가 각 케이스를 독립 테스트로 실행해 어떤 입력에서 실패했는지 명확히 보여준다.
"""

import pytest

# ──── 1. 테스트 대상 함수 ────

def add(a: int, b: int) -> int:
    return a + b


def is_palindrome(s: str) -> bool:
    """문자열이 팰린드롬이면 True."""
    return s == s[::-1]


# ──── 2. 기본 parametrize ────
# 인자 이름을 쉼표로 나열하고, 값은 튜플 리스트로 전달한다.

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a: int, b: int, expected: int):
    # 실패 시 pytest 는 어떤 (a, b, expected) 케이스인지 표시한다
    assert add(a, b) == expected


# ──── 3. 문자열 parametrize ────

@pytest.mark.parametrize("word,result", [
    ("racecar", True),
    ("hello",   False),
    ("level",   True),
    ("",        True),   # 빈 문자열도 팰린드롬
])
def test_is_palindrome(word: str, result: bool):
    assert is_palindrome(word) == result


# ──── 4. ids 로 케이스 이름 지정 ────

@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 15),
    (0,  0,  0),
], ids=["양수 합산", "영 합산"])
def test_add_named(a: int, b: int, expected: int):
    assert add(a, b) == expected


# ──── 5. 실행 ────

if __name__ == "__main__":
    pytest.main(["-q", __file__])
