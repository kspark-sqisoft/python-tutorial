"""
연습문제 04: 집합 연산.
두 리스트의 교집합·합집합·차집합을 구하라.
"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

# TODO 1: a 와 b 의 교집합(공통 원소) inter 를 만드세요.
inter = None

# TODO 2: a 와 b 의 합집합(전체 원소, 중복 없이) union_ 를 만드세요.
union_ = None

# TODO 3: a 에는 있지만 b 에는 없는 원소의 집합 diff 를 만드세요.
diff = None

# ── 검증 ──
assert inter == {3, 4}, f"inter 가 올바르지 않습니다: {inter}"
assert union_ == {1, 2, 3, 4, 5, 6}, f"union_ 이 올바르지 않습니다: {union_}"
assert diff == {1, 2}, f"diff 가 올바르지 않습니다: {diff}"
print("OK")
