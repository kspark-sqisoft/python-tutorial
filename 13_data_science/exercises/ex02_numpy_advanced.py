"""
연습문제 02: numpy 심화
1~12 정수를 3x4 행렬로 reshape 한 뒤
행별 합(row_sums)과 열별 합(col_sums)을 구하세요.
"""

import numpy as np

# ──── TODO ────
# 1. 1~12 정수 배열을 (3, 4) 형태로 reshape 한 mat 을 만드세요
mat = None  # TODO

# 2. 행별 합(각 행의 원소 합, shape (3,)) 을 row_sums 에 저장하세요
row_sums = None  # TODO

# 3. 열별 합(각 열의 원소 합, shape (4,)) 을 col_sums 에 저장하세요
col_sums = None  # TODO

# ──── 검증 (수정 금지) ────
assert mat is not None, "mat 을 정의하세요"
assert mat.shape == (3, 4), f"shape 이 (3,4) 여야 합니다, 현재: {mat.shape}"

assert row_sums is not None, "row_sums 를 정의하세요"
assert list(row_sums) == [10, 26, 42], f"row_sums 가 틀렸습니다: {row_sums}"

assert col_sums is not None, "col_sums 를 정의하세요"
assert list(col_sums) == [15, 18, 21, 24], f"col_sums 가 틀렸습니다: {col_sums}"

print("OK")
