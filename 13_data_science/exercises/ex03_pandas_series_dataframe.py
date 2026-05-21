"""
연습문제 03: pandas Series / DataFrame
주어진 딕셔너리로 DataFrame 을 만들고
"score" 열의 평균을 구하세요.
"""

import pandas as pd

DATA = {
    "name":  ["Alice", "Bob", "Carol", "Dave"],
    "score": [90, 85, 78, 92],
    "team":  ["A", "B", "A", "B"],
}

# ──── TODO ────
# 1. DATA 딕셔너리로 DataFrame df 를 만드세요
df = None  # TODO

# 2. "score" 열의 평균을 mean_score 에 저장하세요
mean_score = None  # TODO

# ──── 검증 (수정 금지) ────
assert df is not None, "df 를 정의하세요"
assert list(df.columns) == ["name", "score", "team"], "열 순서를 확인하세요"
assert len(df) == 4, "행 수는 4여야 합니다"

assert mean_score is not None, "mean_score 를 정의하세요"
assert round(float(mean_score), 2) == 86.25, f"평균이 86.25여야 합니다, 현재: {mean_score}"

print("OK")
