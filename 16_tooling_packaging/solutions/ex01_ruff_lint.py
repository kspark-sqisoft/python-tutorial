"""
정답 01 — ruff 린트
double 함수 구현.
"""


def double(x: int) -> int:
    """정수 x 를 두 배로 만들어 반환한다."""
    return x * 2


if __name__ == "__main__":
    assert double(3) == 6
    assert double(0) == 0
    assert double(-2) == -4
    print("OK")
