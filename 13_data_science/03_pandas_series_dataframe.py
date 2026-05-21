"""
pandas 기초: Series와 DataFrame 생성,
인덱싱(loc/iloc), 열 추가/수정, dtypes, describe 를 다룬다.
표 형태 데이터를 다루는 핵심 자료구조를 이해한다.
"""

import pandas as pd

# ──── 1. Series ────

def section_series() -> None:
    # Series: 인덱스가 붙은 1차원 배열
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print("Series:\n", s)
    print("s['b']:", s["b"])       # 레이블 인덱싱
    print("s[0]:", s.iloc[0])      # 위치 인덱싱
    print("dtype:", s.dtype)


# ──── 2. DataFrame 생성 ────

def section_dataframe_create() -> None:
    # DataFrame: 열(column)이 여러 개인 2차원 표
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave"],
        "score": [90, 85, 78, 92],
        "team":  ["A", "B", "A", "B"],
    })
    print("DataFrame:\n", df)
    print("\nshape:", df.shape)
    print("columns:", df.columns.tolist())
    print("dtypes:\n", df.dtypes)


# ──── 3. 인덱싱: loc / iloc ────

def section_indexing() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave"],
        "score": [90, 85, 78, 92],
        "team":  ["A", "B", "A", "B"],
    })

    # loc: 레이블 기반 (행 레이블, 열 이름)
    print("loc[0, 'name']:", df.loc[0, "name"])
    print("loc[1:2, ['name','score']]:\n", df.loc[1:2, ["name", "score"]])

    # iloc: 위치 기반 (행 번호, 열 번호)
    print("iloc[0, 0]:", df.iloc[0, 0])
    print("iloc[:2, :2]:\n", df.iloc[:2, :2])


# ──── 4. 열 추가·수정 및 describe ────

def section_columns_describe() -> None:
    df = pd.DataFrame({
        "name":  ["Alice", "Bob", "Carol", "Dave"],
        "score": [90, 85, 78, 92],
        "team":  ["A", "B", "A", "B"],
    })

    # 새 열 추가: 점수에서 5점 보너스
    df["bonus"] = df["score"] + 5
    print("bonus 열 추가:\n", df)

    # 열 값 수정
    df["score"] = df["score"] * 1.1   # 10% 인상
    print("\nscore 10% 인상:\n", df)

    # describe: 수치형 열의 기본 통계량
    print("\ndescribe:\n", df.describe())


if __name__ == "__main__":
    print("=" * 45)
    print("1. Series")
    print("=" * 45)
    section_series()

    print("\n" + "=" * 45)
    print("2. DataFrame 생성")
    print("=" * 45)
    section_dataframe_create()

    print("\n" + "=" * 45)
    print("3. 인덱싱: loc / iloc")
    print("=" * 45)
    section_indexing()

    print("\n" + "=" * 45)
    print("4. 열 추가·수정 및 describe")
    print("=" * 45)
    section_columns_describe()
