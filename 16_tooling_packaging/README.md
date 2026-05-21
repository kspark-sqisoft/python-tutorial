# 16_tooling_packaging — 툴링·패키징

## 사전 준비

```bash
uv pip install -e ".[dev]"
uv pip install -e ".[typing]"
```

## 배우는 것

- ruff — 빠른 린트
- black — 의견 강한 포매터
- mypy — 정적 타입 검사 (10_typing 재방문)
- pyproject.toml 해부 (tomllib 으로 읽기 실습)
- uv build / publish — 배포 흐름 맛보기

## 학습 순서

1. `01_ruff_lint.py`
2. `02_black_format.py`
3. `03_mypy_recap.py`
4. `04_pyproject_anatomy.py`
5. `05_packaging_with_uv.py`

## 실행 방법

```bash
uv run python 16_tooling_packaging/01_ruff_lint.py
```

## 도구 사용 (학습자 수동)

```bash
uv run ruff check 16_tooling_packaging/
uv run black --check 16_tooling_packaging/
uv run mypy 16_tooling_packaging/
```

## 연습문제

- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO 채우기.
