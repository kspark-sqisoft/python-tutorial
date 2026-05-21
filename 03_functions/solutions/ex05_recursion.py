"""
정답 05 — 재귀 / deep_sum
왜 이렇게 구현하나:
- 각 요소가 리스트이면 재귀 호출, 숫자이면 그대로 더하는 두 가지 경우로 나눈다.
- isinstance(item, list) 로 타입을 판별해 중첩 구조를 자연스럽게 탐색한다.
- 빈 리스트는 for 루프가 실행되지 않아 0 을 반환하므로 별도 처리가 불필요하다.
"""


def deep_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  # 리스트이면 재귀로 내려간다
            total += deep_sum(item)
        else:                       # 숫자이면 바로 합산
            total += item
    return total


assert deep_sum([1, [2, [3, [4, 5]]], 6]) == 21
assert deep_sum([1, 2, 3])               == 6
assert deep_sum([[1, [2]], [3]])          == 6
assert deep_sum([])                      == 0
print("OK")
