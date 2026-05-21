"""
정답 04 — itertools

chain([1,2], [3,4]) 는 두 리스트를 이어 붙인 이터레이터를 반환한다.
count(0, 2) 는 0, 2, 4, … 무한 수열이므로 islice 로 앞 5개만 잘라낸다.
itertools 함수는 이터레이터를 반환하므로 list() 로 감싸야 리스트가 된다.
"""

import itertools

chained = list(itertools.chain([1, 2], [3, 4]))

first_five_evens = list(itertools.islice(itertools.count(0, 2), 5))

# ──── 검증 (수정 금지) ────
assert chained == [1, 2, 3, 4], \
    f"chain 결과가 올바르지 않습니다: {chained}"
assert first_five_evens == [0, 2, 4, 6, 8], \
    f"islice+count 결과가 올바르지 않습니다: {first_five_evens}"
print("OK")
