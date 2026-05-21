"""
풀이 05 — 실전 패턴 (Callable)
왜: Callable[[int], int] 는 int 를 하나 받아 int 를 반환하는 함수 타입이다.
    apply 는 이 타입의 함수를 받아 x 에 적용한다 — 고차 함수의 타입 안전한 표현.
"""

from typing import Callable


def apply(fn: Callable[[int], int], x: int) -> int:
    """fn 을 x 에 적용한 결과를 반환한다."""
    return fn(x)


assert apply(lambda n: n * 2, 5) == 10
assert apply(lambda n: n + 100, 7) == 107
assert apply(abs, -3) == 3
print("OK")
