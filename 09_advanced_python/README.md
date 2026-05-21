# 09_advanced_python — 데코레이터·컨텍스트·디스크립터·메타클래스

## 배우는 것
- 함수 데코레이터 (단일 / 인자 받는 / functools.wraps)
- 컨텍스트 매니저 (클래스 기반 `__enter__`/`__exit__` + `@contextmanager`)
- 디스크립터 — `@property` 의 정체
- 메타클래스 맛보기 — `type` 으로 클래스 동적 생성

## 학습 순서
1. `01_decorators.py`
2. `02_context_managers.py`
3. `03_descriptors.py`
4. `04_metaclasses_intro.py`

## 실행 방법
```bash
uv run python 09_advanced_python/01_decorators.py
uv run python 09_advanced_python/02_context_managers.py
uv run python 09_advanced_python/03_descriptors.py
uv run python 09_advanced_python/04_metaclasses_intro.py
```

## 연습문제
- `exercises/ex01_*.py` ~ `ex04_*.py` 의 TODO 를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 폴더의 정답과 비교한다.

```bash
uv run python 09_advanced_python/exercises/ex01_decorators.py
uv run python 09_advanced_python/exercises/ex02_context_managers.py
uv run python 09_advanced_python/exercises/ex03_descriptors.py
uv run python 09_advanced_python/exercises/ex04_metaclasses_intro.py
```
