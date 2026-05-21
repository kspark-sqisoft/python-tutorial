"""
연습문제 05 — 재귀
TODO: deep_sum(lst) 를 완성하세요.
- lst 는 숫자와 리스트가 중첩된 구조입니다.
- 모든 깊이의 숫자를 재귀로 합산해 반환하세요.
- 예: deep_sum([1, [2, [3, [4, 5]]], 6]) == 21
"""


def deep_sum(lst):
    # TODO: 구현하세요
    pass


# ── 검증 (수정하지 마세요) ──
assert deep_sum([1, [2, [3, [4, 5]]], 6]) == 21, "중첩 합산 실패"
assert deep_sum([1, 2, 3])               == 6,  "평탄 리스트 실패"
assert deep_sum([[1, [2]], [3]])          == 6,  "2단계 중첩 실패"
assert deep_sum([])                      == 0,  "빈 리스트 실패"
print("OK")
