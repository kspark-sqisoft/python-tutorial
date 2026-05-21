"""
연습문제 01 — ruff 린트
TODO: double 함수를 완성하세요.
완성 후 `uv run ruff check 16_tooling_packaging/exercises/ex01_ruff_lint.py` 로 확인.
"""


def double(x: int) -> int:
    """정수 x 를 두 배로 만들어 반환한다."""
    # TODO: x 의 두 배를 반환하는 코드를 작성하세요.
    raise NotImplementedError


if __name__ == "__main__":
    assert double(3) == 6
    assert double(0) == 0
    assert double(-2) == -4
    print("OK")
