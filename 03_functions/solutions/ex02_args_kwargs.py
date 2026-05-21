"""
정답 02 — *args / **kwargs

왜 이렇게 구현하나:
- sum_all 은 *nums 로 받은 튜플을 내장 sum() 으로 합산한다.
  빈 인자일 때 sum(()) == 0 이므로 별도 처리가 필요 없다.
- kv_keys 는 **kwargs 로 받은 dict 의 키를 sorted() 로 정렬해서 반환한다.
  sorted(딕셔너리) 는 키 리스트를 정렬해서 돌려준다 (값은 보지 않는다).
"""


def sum_all(*nums):
    return sum(nums)              # 빈 튜플이면 0 반환


def kv_keys(**kwargs):
    return sorted(kwargs)         # dict 를 sorted 에 넘기면 키가 정렬된 list 로 반환


assert sum_all(1, 2, 3)        == 6
assert sum_all(10, 20, 30, 40) == 100
assert sum_all()               == 0

assert kv_keys(banana=2, apple=5, kiwi=1) == ["apple", "banana", "kiwi"]
assert kv_keys()                          == []

print("OK")
