# 10_typing — 타입 힌트

## 사전 준비

```bash
uv pip install -e ".[typing]"
```

## 배우는 것

- 기본 힌트 (변수/함수/컨테이너/X|None)
- TypedDict 와 Protocol (구조적 부분 타입)
- 제네릭 (Python 3.12 PEP 695 신문법: `def f[T](...)`, `class C[T]:`)
- mypy 로 정적 검증
- 실전 패턴 (Callable / Literal / Final / cast)

## 학습 순서

1. `01_basic_hints.py`
2. `02_typed_dict_protocol.py`
3. `03_generics.py`
4. `04_mypy_check.py`
5. `05_real_world_patterns.py`

## 실행 방법

```bash
uv run python 10_typing/01_basic_hints.py
```

## mypy 로 정적 검증

```bash
uv run mypy 10_typing/
```

## 연습문제

- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO 를 채워 `OK` 가 출력되게 만든다.
- 풀이 후 `uv run mypy 10_typing/solutions/` 가 깨끗해야 한다.
