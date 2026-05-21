"""
정답 03 — mypy 타입 검사
is_positive 함수 구현.
"""


def is_positive(x: float) -> bool:
    """x 가 0 보다 크면 True, 그렇지 않으면 False 를 반환한다."""
    return x > 0


if __name__ == "__main__":
    assert is_positive(1.5) is True
    assert is_positive(0.0) is False
    assert is_positive(-3.0) is False
    print("OK")
