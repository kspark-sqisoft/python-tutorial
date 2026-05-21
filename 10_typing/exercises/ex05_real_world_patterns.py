"""
연습문제 05 — 실전 패턴 (Callable)
TODO: apply 함수를 Callable 힌트와 함께 작성하라.
"""

from typing import Callable

# ──── TODO ────
# apply 함수를 작성하라.
# fn: Callable[[int], int] — 정수를 받아 정수를 반환하는 함수
# x: int — 적용할 값
# 반환: fn(x) 결과
#
# def apply(fn: Callable[[int], int], x: int) -> int:
#     ...

def apply(fn, x):  # type: ignore[empty-body]
    raise NotImplementedError("TODO: Callable 힌트와 함께 구현하세요")


# ──── 검증 ────
assert apply(lambda n: n * 2, 5) == 10
assert apply(lambda n: n + 100, 7) == 107
assert apply(abs, -3) == 3
print("OK")
