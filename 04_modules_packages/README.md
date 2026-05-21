# 04_modules_packages — 모듈과 패키지

## 배우는 것
- import 4가지 형태 (import, from, as)
- 표준 라이브러리 맛보기: pathlib, datetime, random, math
- 자체 패키지 만들기 (`mypkg/__init__.py`, 하위 모듈)

## 학습 순서
1. `01_import_basics.py`
2. `02_stdlib_pathlib.py`
3. `03_stdlib_datetime.py`
4. `04_stdlib_random_math.py`
5. `05_making_modules.py`

## 폴더 구조
```
04_modules_packages/
├─ 01_import_basics.py
├─ 02_stdlib_pathlib.py
├─ 03_stdlib_datetime.py
├─ 04_stdlib_random_math.py
├─ 05_making_modules.py
└─ mypkg/
    ├─ __init__.py
    ├─ greet.py
    └─ calc.py
```

## 실행 방법
```bash
uv run python 04_modules_packages/05_making_modules.py
```

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- ex05 는 같은 폴더의 `_my_module.py` 를 import 해서 푼다.
- 막히면 `solutions/` 와 비교.
