"""
연습문제 03 — mypy 타입 검사
TODO: is_positive 함수를 완성하세요.
완성 후 `uv run mypy 16_tooling_packaging/exercises/ex03_mypy_recap.py` 로 확인.
"""


def is_positive(x: float) -> bool:
    """x 가 0 보다 크면 True, 그렇지 않으면 False 를 반환한다."""
    # TODO: x > 0 이면 True, 아니면 False 를 반환하는 코드를 작성하세요.
    raise NotImplementedError


if __name__ == "__main__":
    assert is_positive(1.5) is True
    assert is_positive(0.0) is False
    assert is_positive(-3.0) is False
    print("OK")
