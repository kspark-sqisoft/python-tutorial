"""
정답 02 — *args / **kwargs
왜 이렇게 구현하나:
- sum_all 은 *nums 로 받은 튜플을 내장 sum() 으로 합산한다.
  빈 인자일 때 sum(()) == 0 이므로 별도 처리가 필요 없다.
- print_kv 는 sorted(kwargs) 로 키를 정렬하고 출력 후 리스트를 반환한다.
  딕셔너리를 sorted() 에 넘기면 키 목록이 정렬되어 나온다.
"""


def sum_all(*nums):
    return sum(nums)          # 빈 튜플이면 0 반환


def print_kv(**kwargs):
    keys = sorted(kwargs)     # 딕셔너리 → 정렬된 키 리스트
    for k in keys:
        print(f"{k}={kwargs[k]}")
    return keys


assert sum_all(1, 2, 3)        == 6
assert sum_all(10, 20, 30, 40) == 100
assert sum_all()               == 0

import io, sys
buf = io.StringIO()
sys.stdout = buf
keys = print_kv(banana=2, apple=5, kiwi=1)
sys.stdout = sys.__stdout__
assert keys == ["apple", "banana", "kiwi"]
print("OK")
