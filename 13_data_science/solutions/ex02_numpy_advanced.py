"""
정답 02: numpy 심화
"""

import numpy as np

mat = np.arange(1, 13).reshape((3, 4))   # 1~12 → (3,4)
row_sums = mat.sum(axis=1)               # 행별 합 (axis=1)
col_sums = mat.sum(axis=0)               # 열별 합 (axis=0)

assert mat.shape == (3, 4)
assert list(row_sums) == [10, 26, 42]
assert list(col_sums) == [15, 18, 21, 24]

print("OK")
