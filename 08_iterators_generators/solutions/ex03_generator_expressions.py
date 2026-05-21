"""
정답 03 — 제너레이터 표현식

(x*x for x in range(1, 101)) 은 제너레이터 표현식이다.
sum() 에 직접 넘기면 중간 리스트를 만들지 않고 합산할 수 있다.
1² + 2² + … + 100² = n(n+1)(2n+1)/6 = 338350.
"""

sum_squares = sum(x * x for x in range(1, 101))

# ──── 검증 (수정 금지) ────
assert sum_squares == 338350, \
    f"합이 올바르지 않습니다. 실제: {sum_squares}"
print("OK")
