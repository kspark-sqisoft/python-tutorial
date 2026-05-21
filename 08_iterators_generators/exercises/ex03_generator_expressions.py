"""
연습문제 03 — 제너레이터 표현식
generator expression 을 사용해 1~100 의 제곱 합을 계산한다.
"""

# ──── TODO ────
# generator expression 을 사용해 1 부터 100 까지 각 수의 제곱 합을 구하라.
# sum() 함수에 generator expression 을 직접 넘겨야 한다.
# 리스트 컴프리헨션 [ ] 사용 금지.

sum_squares = 0  # TODO: sum(... generator expression ...)

# ──── 검증 (수정 금지) ────
assert sum_squares == 338350, \
    f"합이 올바르지 않습니다. 실제: {sum_squares}"
print("OK")
