"""
정답 01: numpy 기초
"""

import numpy as np

arr = np.arange(1, 11)          # 1~10 정수 배열
mean_val = arr.mean()            # 평균
std_val = arr.std()              # 표준편차
max_val = arr.max()              # 최댓값

assert len(arr) == 10
assert round(float(mean_val), 1) == 5.5
assert round(float(std_val), 4) == round(float(np.std(np.arange(1, 11))), 4)
assert int(max_val) == 10

print("OK")
