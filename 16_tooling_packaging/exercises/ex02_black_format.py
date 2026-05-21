"""
연습문제 02 — black 포매터
TODO: square 함수를 완성하세요.
완성 후 `uv run black --check 16_tooling_packaging/exercises/ex02_black_format.py` 로 확인.
"""


def square(x: int) -> int:
    """정수 x 의 제곱을 반환한다."""
    # TODO: x 의 제곱을 반환하는 코드를 작성하세요.
    raise NotImplementedError


if __name__ == "__main__":
    assert square(4) == 16
    assert square(0) == 0
    assert square(-3) == 9
    print("OK")
