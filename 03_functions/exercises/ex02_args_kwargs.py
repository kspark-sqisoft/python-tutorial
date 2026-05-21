"""
연습문제 02 — *args / **kwargs

TODO 1: sum_all(*nums) — 전달받은 모든 숫자의 합을 반환.
TODO 2: kv_keys(**kwargs) — 전달받은 키워드 인자들의 키 목록을 정렬해서 반환.

힌트:
- *nums 는 튜플로 모인다 — sum() 으로 합산 가능.
- **kwargs 는 dict 로 모인다 — sorted(kwargs) 가 키 리스트를 정렬해서 반환.

모든 assert 가 통과하면 "OK" 가 출력됩니다.
"""


def sum_all(*nums):
    # TODO: 구현하세요
    pass


def kv_keys(**kwargs):
    # TODO: 키 목록을 정렬해서 반환하세요
    pass


# ── 채점 (수정 금지) ──
assert sum_all(1, 2, 3)        == 6,    "합산 테스트 실패"
assert sum_all(10, 20, 30, 40) == 100,  "합산 테스트 실패"
assert sum_all()               == 0,    "빈 인자 테스트 실패"

assert kv_keys(banana=2, apple=5, kiwi=1) == ["apple", "banana", "kiwi"], "정렬 키 반환 테스트 실패"
assert kv_keys()                          == [],                          "빈 kwargs 테스트 실패"

print("OK")
