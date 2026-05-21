"""
풀이 03 — 제네릭 (PEP 695 신문법)
왜: PEP 695 (Python 3.12+) 는 TypeVar 선언 없이 def f[T](...) 문법으로
    타입 매개변수를 인라인으로 선언한다. T | None 반환으로 빈 리스트를 안전하게 처리한다.
"""


def last[T](items: list[T]) -> T | None:
    """리스트의 마지막 원소를 반환한다. 빈 리스트면 None."""
    return items[-1] if items else None


assert last([1, 2, 3]) == 3
assert last(["a", "b", "c"]) == "c"
assert last([]) is None
print("OK")
