"""
정답 04: pandas IO / 필터 / groupby
"""

import tempfile
import pandas as pd

DATA = {
    "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "score": [90, 85, 78, 92, 88],
    "team":  ["A", "B", "A", "B", "A"],
}

with tempfile.TemporaryDirectory() as tmpdir:
    csv_path = f"{tmpdir}/scores.csv"

    df = pd.DataFrame(DATA)
    df.to_csv(csv_path, index=False)

    loaded_df = pd.read_csv(csv_path)

    team_avg = loaded_df.groupby("team")["score"].mean().to_dict()

    assert len(loaded_df) == 5
    assert round(team_avg["A"], 2) == round((90 + 78 + 88) / 3, 2)
    assert round(team_avg["B"], 2) == round((85 + 92) / 2, 2)

    print("OK")
