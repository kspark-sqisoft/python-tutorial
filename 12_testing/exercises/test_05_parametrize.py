"""
연습 05 — parametrize.
@pytest.mark.parametrize 는 설정되어 있다.
test_multiply 함수 본문의 TODO 를 채워 모든 케이스를 통과시켜라.
"""

import pytest


def multiply(a: int, b: int) -> int:
    return a * b


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-1, 4, -4),
])
def test_multiply(a: int, b: int, expected: int):
    # TODO: multiply(a, b) 의 결과가 expected 임을 assert 로 검증하라.
    assert False, "TODO: assert multiply(a, b) == expected 를 작성하라"
