"""
정답 02 — yield 와 제너레이터 함수

yield 키워드를 사용하면 함수가 제너레이터 함수가 된다.
호출 시 제너레이터 객체가 반환되고, 본문은 lazy 하게 실행된다.
짝수 조건(i % 2 == 0)을 확인하면서 n 미만 범위를 순회하면 된다.
"""

def even_until(n):
    """0 부터 n 미만의 짝수를 yield 한다."""
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i += 1

# ──── 검증 (수정 금지) ────
assert list(even_until(10)) == [0, 2, 4, 6, 8], \
    f"결과가 올바르지 않습니다: {list(even_until(10))}"
assert list(even_until(0)) == [], \
    "even_until(0) 은 빈 리스트여야 합니다."
assert list(even_until(6)) == [0, 2, 4], \
    f"even_until(6) 결과가 올바르지 않습니다."
print("OK")
