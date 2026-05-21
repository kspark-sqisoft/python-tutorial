"""
연습문제 04 — itertools
itertools.chain 과 itertools.islice + itertools.count 를 사용한다.
"""

import itertools

# ──── TODO 1: chain ────
# itertools.chain 을 사용해 [1, 2] 와 [3, 4] 를 이어 붙인다.

chained = []  # TODO: list(itertools.chain(...))

# ──── TODO 2: islice + count ────
# itertools.count(0, 2) 로 0부터 2씩 증가하는 무한 수열을 만들고
# itertools.islice 로 앞 5개만 잘라낸다.

first_five_evens = []  # TODO: list(itertools.islice(itertools.count(...), ...))

# ──── 검증 (수정 금지) ────
assert chained == [1, 2, 3, 4], \
    f"chain 결과가 올바르지 않습니다: {chained}"
assert first_five_evens == [0, 2, 4, 6, 8], \
    f"islice+count 결과가 올바르지 않습니다: {first_five_evens}"
print("OK")
