"""
정답 02 — black 포매터
square 함수 구현.
"""


def square(x: int) -> int:
    """정수 x 의 제곱을 반환한다."""
    return x * x


if __name__ == "__main__":
    assert square(4) == 16
    assert square(0) == 0
    assert square(-3) == 9
    print("OK")
