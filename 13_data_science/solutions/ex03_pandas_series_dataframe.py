"""
정답 03: pandas Series / DataFrame
"""

import pandas as pd

DATA = {
    "name":  ["Alice", "Bob", "Carol", "Dave"],
    "score": [90, 85, 78, 92],
    "team":  ["A", "B", "A", "B"],
}

df = pd.DataFrame(DATA)
mean_score = df["score"].mean()

assert list(df.columns) == ["name", "score", "team"]
assert len(df) == 4
assert round(float(mean_score), 2) == 86.25

print("OK")
