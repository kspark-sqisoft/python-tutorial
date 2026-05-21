"""
연습문제 01: 리스트 생성과 필터링.
1~10 정수 리스트를 만들고, 짝수만 컴프리헨션으로 추출하라.
"""

# TODO 1: 1부터 10까지의 정수를 담은 리스트 nums 를 만드세요.
#         힌트: range() 와 list() 를 활용하세요.
nums = None

# TODO 2: 컴프리헨션을 사용해 nums 에서 짝수만 모은 리스트 evens 를 만드세요.
#         짝수 조건: x % 2 == 0
evens = None

# ── 검증 ──
assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f"nums 가 올바르지 않습니다: {nums}"
assert evens == [2, 4, 6, 8, 10], f"evens 가 올바르지 않습니다: {evens}"
print("OK")
