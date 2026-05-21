"""
연습문제 02 — yield 와 제너레이터 함수
0 부터 n 미만의 짝수를 yield 하는 제너레이터 함수를 작성한다.
"""

# ──── TODO ────
# even_until(n) 제너레이터 함수를 완성하라.
# 0, 2, 4, … n 미만의 짝수를 하나씩 yield 해야 한다.

def even_until(n):
    """0 부터 n 미만의 짝수를 yield 한다."""
    pass  # TODO: yield 를 사용해 구현

# ──── 검증 (수정 금지) ────
assert list(even_until(10)) == [0, 2, 4, 6, 8], \
    f"결과가 올바르지 않습니다: {list(even_until(10))}"
assert list(even_until(0)) == [], \
    "even_until(0) 은 빈 리스트여야 합니다."
assert list(even_until(6)) == [0, 2, 4], \
    f"even_until(6) 결과가 올바르지 않습니다."
print("OK")
