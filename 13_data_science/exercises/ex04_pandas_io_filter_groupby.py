"""
연습문제 04: pandas IO / 필터 / groupby
tempfile 에 CSV 를 저장한 뒤 read_csv 로 읽고
팀별 평균 점수 딕셔너리를 만드세요.
"""

import tempfile
import pandas as pd

DATA = {
    "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "score": [90, 85, 78, 92, 88],
    "team":  ["A", "B", "A", "B", "A"],
}

# ──── TODO ────
with tempfile.TemporaryDirectory() as tmpdir:
    csv_path = f"{tmpdir}/scores.csv"

    # 1. DATA 로 DataFrame 을 만들고 csv_path 에 CSV 로 저장하세요 (index=False)
    # TODO

    # 2. csv_path 에서 CSV 를 읽어 loaded_df 에 저장하세요
    loaded_df = None  # TODO

    # 3. 팀별 "score" 평균을 구해 딕셔너리 team_avg 로 만드세요
    #    예: {"A": 85.33..., "B": 88.5}
    team_avg = None  # TODO

    # ──── 검증 (수정 금지) ────
    assert loaded_df is not None, "loaded_df 를 정의하세요"
    assert len(loaded_df) == 5, "행 수는 5여야 합니다"

    assert team_avg is not None, "team_avg 를 정의하세요"
    assert round(team_avg["A"], 2) == round((90 + 78 + 88) / 3, 2), f"A 팀 평균이 틀렸습니다: {team_avg['A']}"
    assert round(team_avg["B"], 2) == round((85 + 92) / 2, 2), f"B 팀 평균이 틀렸습니다: {team_avg['B']}"

    print("OK")
