"""
연습문제 02 — *args / **kwargs
TODO 1: sum_all(*nums) — 전달받은 모든 숫자의 합을 반환하세요.
TODO 2: print_kv(**kwargs) — 키를 정렬한 뒤 "key=value" 형식으로
        각 항목을 출력하고, 정렬된 키 리스트를 반환하세요.
"""


def sum_all(*nums):
    # TODO: 구현하세요
    pass


def print_kv(**kwargs):
    # TODO: 키를 정렬하여 출력하고 정렬된 키 리스트를 반환하세요
    pass


# ── 검증 (수정하지 마세요) ──
assert sum_all(1, 2, 3)        == 6,  "합산 테스트 실패"
assert sum_all(10, 20, 30, 40) == 100, "합산 테스트 실패"
assert sum_all()               == 0,  "빈 인자 테스트 실패"

keys = print_kv(banana=2, apple=5, kiwi=1)
assert keys == ["apple", "banana", "kiwi"], "정렬 키 반환 테스트 실패"
print("OK")
