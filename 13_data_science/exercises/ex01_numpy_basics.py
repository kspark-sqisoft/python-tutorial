"""
연습문제 01: numpy 기초
1~10 정수 배열을 만들고 평균, 표준편차, 최댓값을 구하세요.
"""

import numpy as np

# ──── TODO ────
# 1. 1~10 정수 배열 arr 을 만드세요 (np.arange 사용)
arr = None  # TODO

# 2. arr 의 평균을 mean_val 에 저장하세요
mean_val = None  # TODO

# 3. arr 의 표준편차를 std_val 에 저장하세요
std_val = None  # TODO

# 4. arr 의 최댓값을 max_val 에 저장하세요
max_val = None  # TODO

# ──── 검증 (수정 금지) ────
assert arr is not None, "arr 을 정의하세요"
assert len(arr) == 10, "arr 길이는 10이어야 합니다"
assert round(float(mean_val), 1) == 5.5, f"평균이 5.5여야 합니다, 현재: {mean_val}"
assert round(float(std_val), 4) == round(float(np.std(np.arange(1, 11))), 4), "표준편차를 확인하세요"
assert int(max_val) == 10, "최댓값은 10이어야 합니다"

print("OK")
