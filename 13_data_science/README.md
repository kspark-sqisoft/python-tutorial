# 13_data_science — 데이터 분석 (numpy / pandas / matplotlib)

## 사전 준비

```bash
uv pip install -e ".[data]"
```

## 배우는 것

- numpy: 배열 생성·벡터화 연산·브로드캐스팅·집계·랜덤
- pandas: Series / DataFrame 기본, IO, 필터, groupby
- matplotlib: 헤드리스 모드 (Agg) + savefig (모든 IO 는 tempfile)

## 학습 순서

1. `01_numpy_basics.py`
2. `02_numpy_advanced.py`
3. `03_pandas_series_dataframe.py`
4. `04_pandas_io_filter_groupby.py`
5. `05_matplotlib_intro.py`

## 실행 방법

```bash
uv run python 13_data_science/01_numpy_basics.py
```

## 연습문제

- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO 채우기.
- 모든 IO 는 임시 파일/디렉터리 — 저장소에 잔여물 없음.
