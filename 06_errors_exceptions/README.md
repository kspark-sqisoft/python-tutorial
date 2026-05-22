# 06_errors_exceptions — 예외 처리

## 배우는 것
- try / except / else / finally
- raise 와 사용자 정의 예외 (Exception 상속)
- 자주 보는 예외 계층 (Exception 자식들)
- EAFP (Easier to Ask Forgiveness than Permission) vs LBYL — 파이썬 관용
- 예외 chaining — `raise X from Y`, `__cause__`/`__context__`, `from None`, `ExceptionGroup`/`except*` (Dart/TS 비교)

## 학습 순서
1. `01_try_except.py`
2. `02_else_finally.py`
3. `03_raise_custom.py`
4. `04_exception_hierarchy.py`
5. `05_eafp.py`
6. `06_chaining.py`

## 실행 방법
```bash
uv run python 06_errors_exceptions/01_try_except.py
```

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 와 비교.
