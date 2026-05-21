"""
연습문제 03 — 제네릭 (PEP 695 신문법)
TODO: last 함수를 PEP 695 신문법으로 작성하라.
"""

# ──── TODO ────
# PEP 695 신문법으로 아래 함수를 작성하라:
#   def last[T](items: list[T]) -> T | None:
#       리스트의 마지막 원소를 반환한다.
#       빈 리스트면 None 을 반환한다.

def last(items):  # type: ignore[empty-body]
    raise NotImplementedError("TODO: PEP 695 제네릭 문법으로 구현하세요")


# ──── 검증 ────
assert last([1, 2, 3]) == 3
assert last(["a", "b", "c"]) == "c"
assert last([]) is None
print("OK")
