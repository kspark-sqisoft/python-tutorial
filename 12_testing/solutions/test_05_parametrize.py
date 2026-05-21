"""
정답 05 — parametrize.
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
    assert multiply(a, b) == expected
