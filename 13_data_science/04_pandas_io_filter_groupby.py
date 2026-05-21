"""
pandas IO·필터·groupby: CSV 읽기/쓰기,
조건 필터, 정렬, groupby+agg 를 다룬다.
모든 파일 IO 는 tempfile 안에서 처리한다.
"""

import tempfile
import pandas as pd

# ──── 1. CSV IO ────

def section_csv_io() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "score": [90, 85, 78, 92, 88],
        "team":  ["A", "B", "A", "B", "A"],
    })

    with tempfile.TemporaryDirectory() as tmpdir:
        path = f"{tmpdir}/scores.csv"

        # CSV 저장
        df.to_csv(path, index=False)
        print(f"CSV 저장 완료: {path}")

        # CSV 읽기
        loaded = pd.read_csv(path)
        print("CSV 읽기:\n", loaded)
        print("dtypes:\n", loaded.dtypes)


# ──── 2. 필터링 ────

def section_filter() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "score": [90, 85, 78, 92, 88],
        "team":  ["A", "B", "A", "B", "A"],
    })

    # 단일 조건
    high = df[df["score"] > 85]
    print("score > 85:\n", high)

    # 복합 조건: & (and), | (or)
    filtered = df[(df["score"] >= 85) & (df["team"] == "A")]
    print("score>=85 AND team='A':\n", filtered)


# ──── 3. 정렬 ────

def section_sort() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "score": [90, 85, 78, 92, 88],
        "team":  ["A", "B", "A", "B", "A"],
    })

    # 점수 내림차순 정렬
    sorted_df = df.sort_values("score", ascending=False)
    print("점수 내림차순:\n", sorted_df)

    # 복수 열 정렬: team 오름차순 → score 내림차순
    multi = df.sort_values(["team", "score"], ascending=[True, False])
    print("team↑ score↓:\n", multi)


# ──── 4. groupby + agg ────

def section_groupby() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "score": [90, 85, 78, 92, 88],
        "team":  ["A", "B", "A", "B", "A"],
    })

    # 팀별 평균 점수
    team_mean = df.groupby("team")["score"].mean()
    print("팀별 평균 점수:\n", team_mean)

    # 여러 집계 함수 동시 적용
    team_agg = df.groupby("team")["score"].agg(["mean", "max", "count"])
    print("팀별 집계(mean/max/count):\n", team_agg)


if __name__ == "__main__":
    print("=" * 45)
    print("1. CSV IO")
    print("=" * 45)
    section_csv_io()

    print("\n" + "=" * 45)
    print("2. 필터링")
    print("=" * 45)
    section_filter()

    print("\n" + "=" * 45)
    print("3. 정렬")
    print("=" * 45)
    section_sort()

    print("\n" + "=" * 45)
    print("4. groupby + agg")
    print("=" * 45)
    section_groupby()
