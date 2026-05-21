# Python Tutorial — 설계 문서

- 작성일: 2026-05-21
- 작성자: Kee Soon Park (ks.park@sqisoft.com)
- 상태: 승인됨 (브레인스토밍 완료, 구현 계획 단계로 진행)

## 1. 학습자 프로필과 목표

### 1.1 학습자 프로필
- 다른 언어(예: Java/C/JS 계열) 경험 보유, 파이썬은 처음.
- 따라서 "변수/조건/반복/함수"는 압축하고, **파이썬 특유의 idiom과 다른 언어와의 차이**에 비중을 둔다 (truthy/falsy, EAFP, 컴프리헨션, 언패킹, duck typing 등).

### 1.2 학습 범위
- 기초 자료형 → 자료구조 → 함수 → 모듈/패키지
- 객체지향 (클래스, 매직 메서드, dataclass, property)
- 예외, IO, 이터레이터/제너레이터
- 고급(데코레이터, 컨텍스트 매니저, descriptor, 메타클래스 맛보기)
- 타입 힌트, 동시성(threading/multiprocessing/asyncio)
- 실전 라이브러리: 데이터(numpy/pandas/matplotlib), 웹(FastAPI/requests/pydantic), 자동화(argparse/BeautifulSoup/subprocess), 테스트(pytest), 패키징/툴링(uv/ruff/black/mypy)
- 옵션: capstone 미니 프로젝트(1~2개)

### 1.3 비목표 (Non-goals)
- 한 분야를 깊게 파는 것이 아니다 — 각 라이브러리는 "대표 사용 패턴"까지만.
- 컴퓨터 과학 일반(자료구조 이론, 알고리즘 풀이) 강의가 아니다.
- 영문 공식 문서를 대체하지 않는다 — 학습자가 공식 문서로 점프할 수 있는 가교 역할.

## 2. 형식과 톤

### 2.1 파일 형식
- 자료는 `.py` 스크립트 중심.
- `13_data_science`만 일부 `.ipynb` 허용(표·그래프 인라인 확인이 큰 가치).
- 폴더당 `README.md` 1개로 개요·순서·실행법 통일.

### 2.2 주석 언어
- 주석과 README는 **한국어**.
- 코드 식별자(변수·함수·클래스명)는 영어 — 실무 통용 형태 유지.

### 2.3 주석 4원칙 (모든 `.py`에 적용)
1. 상단 모듈 docstring — 다루는 개념과 다른 언어와의 차이를 3~5줄로 요약.
2. 블록마다 `# ──── 제목 ────` 구분선.
3. 개념 첫 등장 시 줄 단위 주석. 반복되는 부분은 생략해 노이즈를 줄인다.
4. 파일 끝에 `if __name__ == "__main__":` 데모 블록 — `uv run python ...`로 바로 실행 가능.

### 2.4 파일 스타일 예시 (학습 자료 톤의 표준)

```python
"""변수와 동적 타이핑.

다른 언어와의 차이점:
- C/Java처럼 타입을 미리 선언하지 않는다 (`int x = 1` ❌, `x = 1` ⭕).
- 변수는 "값을 가리키는 이름표"라고 보는 게 정확하다.
- 같은 이름에 다른 타입의 값을 다시 대입할 수 있다 (런타임 타입).
"""

# ──── 1. 기본 대입 ────

age = 30                          # 정수(int)를 가리키는 이름 `age`
name = "Kee"                      # 문자열(str)을 가리키는 이름 `name`
is_active = True                  # 불리언(bool). 첫 글자가 대문자임에 주의

age = "서른"                       # 같은 이름에 다른 타입 재대입도 합법 — 권장은 X

# ──── 2. 여러 개를 한 줄에 ────

x, y, z = 1, 2, 3                 # 튜플 언패킹 — 다른 언어에 잘 없는 강력한 문법
a = b = c = 0                     # 셋 다 같은 객체를 가리킨다

# ──── 3. 타입 확인 ────

print(type(name))                 # <class 'str'>
print(isinstance(age, str))       # True


# ──── 데모 실행 ────
if __name__ == "__main__":
    print(f"name={name!r}, age={age!r}, is_active={is_active}")
```

## 3. 전체 커리큘럼

총 17개 학습 폴더 + 환경 설정 폴더.

```
python-tutorial/
├─ README.md                       # 전체 학습 가이드 + uv 설치 + 학습 순서
├─ pyproject.toml                  # uv 의존성 관리 (Phase별 extras로 그룹화)
├─ .python-version                 # 파이썬 3.12 고정
│
├─ 00_setup/                       # uv 세팅, Hello World, 실행 방법
│
├─ 01_basics/                      ── Phase 1: 기초
│   ├─ 01_variables.py             # 변수, 동적 타이핑
│   ├─ 02_numbers.py               # int, float, complex, 연산자
│   ├─ 03_strings.py               # f-string, 슬라이싱, 메서드
│   ├─ 04_booleans.py              # truthy/falsy
│   ├─ 05_control_flow.py          # if/elif/else, while, for, match
│   ├─ 06_io.py                    # print, input, 포맷팅
│   ├─ exercises/, solutions/, README.md
│
├─ 02_data_structures/             # list, tuple, dict, set, 컴프리헨션, 슬라이싱
├─ 03_functions/                   # 함수, *args/**kwargs, lambda, scope, 클로저
├─ 04_modules_packages/            # import, pathlib, datetime, math, random
│
├─ 05_oop/                         ── Phase 2: 중급
│   ├─ 01_classes.py
│   ├─ 02_inheritance.py
│   ├─ 03_magic_methods.py
│   ├─ 04_dataclass.py
│   ├─ 05_property.py
│
├─ 06_errors_exceptions/           # try/except, 예외 계층, EAFP vs LBYL
├─ 07_io_files/                    # open, with, JSON, CSV, pathlib
├─ 08_iterators_generators/        # iter/next, yield, itertools
│
├─ 09_advanced_python/             ── Phase 3: 고급
│   ├─ 01_decorators.py
│   ├─ 02_context_managers.py
│   ├─ 03_descriptors.py
│   ├─ 04_metaclasses_intro.py
│
├─ 10_typing/                      # type hint, mypy, Protocol, Generic, TypedDict
├─ 11_concurrency/                 # threading, multiprocessing, asyncio
│
├─ 12_testing/                     ── Phase 4: 실전·라이브러리
│   ├─ 01_unittest_basics.py
│   ├─ 02_pytest_basics.py
│   ├─ 03_fixtures.py
│   ├─ 04_mocking.py
│
├─ 13_data_science/                # numpy, pandas, matplotlib (일부 .ipynb 허용)
├─ 14_web_backend/                 # requests, FastAPI 기초, pydantic
├─ 15_automation/                  # argparse, BeautifulSoup, subprocess, os 자동화
├─ 16_tooling_packaging/           # ruff, black, mypy, pyproject.toml, uv 배포
│
└─ 17_capstone/                    # 옵션: 미니 프로젝트 1~2개 (CLI 도구 + 간단 API)
```

### 3.1 폴더별 단위 (Unit) 정의
각 학습 폴더는 다음 3종 산출물의 조합으로 정의된다.

- 학습 스크립트: `NN_topic.py` (각 파일은 한 가지 핵심 개념만 다룬다)
- 연습문제: `exercises/exNN_topic.py` (TODO + assert 자가 채점)
- 정답: `solutions/exNN_topic.py` (상단에 풀이 의도 docstring)
- 개요: `README.md` (학습 목표, 학습 순서, 실행 방법, 연습 방식)

폴더당 학습 스크립트 5~8개, 연습문제는 핵심 파일 기준으로 5~10개를 기본선으로 한다.

## 4. README 템플릿 (폴더 단위)

폴더별 README는 4단 구성으로 통일한다.

```markdown
# 02_data_structures — 자료구조

## 배우는 것
- list, tuple, dict, set의 차이와 언제 무엇을 쓰나
- 컴프리헨션과 슬라이싱이 왜 강력한가
- 가변(mutable) vs 불변(immutable)

## 학습 순서
1. `01_list.py`
2. `02_tuple.py`
3. `03_dict.py`
4. `04_set.py`
5. `05_comprehensions.py`
6. `06_slicing.py`

## 실행 방법
uv run python 02_data_structures/01_list.py

## 연습문제
- exercises/ 폴더의 TODO를 채우고 직접 실행
- 막히면 solutions/ 같은 번호 파일과 비교
```

## 5. 연습문제 형식

`exercises/ex01_*.py`는 TODO 채우기 + assert 자가 채점 패턴을 따른다.

```python
"""연습 1: list 기초.

아래 TODO를 채워서
`uv run python 02_data_structures/exercises/ex01_list.py`
실행 시 'OK'가 출력되도록 만드세요.
"""

# TODO 1: 1~10 정수가 담긴 리스트를 만들어 `nums`에 할당하세요.
nums = ...

# TODO 2: nums에서 짝수만 골라 `evens`에 담으세요. (컴프리헨션 권장)
evens = ...

assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert evens == [2, 4, 6, 8, 10]
print("OK")
```

`solutions/`에는 같은 파일을 채운 정답을 두고, 상단 docstring에 "왜 이렇게 풀었나"를 한 문단으로 기술한다.

## 6. 환경과 의존성 관리

### 6.1 도구
- `uv` (Rust 기반, 최신 표준)로 venv·패키지·실행을 일원화한다.
- 파이썬 버전: 3.12 (`.python-version`에 고정).

### 6.2 `pyproject.toml` 의존성 그룹화
Phase별로 필요한 라이브러리가 다르므로, optional-dependencies로 그룹을 나눠 진입 시점에 설치한다.

```toml
[project]
name = "python-tutorial"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []                                   # Phase 1~3은 표준 라이브러리만

[project.optional-dependencies]
data    = ["numpy", "pandas", "matplotlib", "jupyter"]                 # 13_data_science
web     = ["fastapi", "uvicorn", "requests", "pydantic", "sqlalchemy"] # 14_web_backend
auto    = ["beautifulsoup4", "click"]                                  # 15_automation
test    = ["pytest", "pytest-cov"]                                     # 12_testing
typing  = ["mypy"]                                                     # 10_typing
dev     = ["ruff", "black"]                                            # 16_tooling_packaging
```

### 6.3 학습 흐름과 설치 시점
```
uv venv                                  # Phase 0: 최초 1회
uv sync                                  # Phase 1~3: 기본만
uv pip install -e ".[test]"              # 12_testing 진입 시
uv pip install -e ".[typing]"            # 10_typing 진입 시
uv pip install -e ".[data]"              # 13_data_science 진입 시
uv pip install -e ".[web]"               # 14_web_backend 진입 시
uv pip install -e ".[auto]"              # 15_automation 진입 시
uv pip install -e ".[dev]"               # 16_tooling_packaging 진입 시
```

이 방식 자체가 "파이썬 의존성을 어떻게 다루는가" 학습의 일부가 된다.

## 7. 제작 진행 방식 (Phase별 단계 제작)

전체 폴더 구조와 `pyproject.toml`은 Phase 0에서 한 번에 확정한다.
이후 콘텐츠 작성은 Phase 단위로 끊어서 진행하며, 각 Phase 종료 시 사용자가 검토한다.

- Phase 0 — 골격 구축: 루트 `README.md`, `pyproject.toml`, `.python-version`, 17개 폴더 + 폴더별 `README.md` 초안 + 빈 `exercises/`, `solutions/`.
- Phase 1 — `01_basics` ~ `04_modules_packages` 완성.
- Phase 2 — `05_oop` ~ `08_iterators_generators` 완성.
- Phase 3 — `09_advanced_python` ~ `11_concurrency` 완성.
- Phase 4 — `12_testing` ~ `16_tooling_packaging` 완성.
- Phase 5 (옵션) — `17_capstone`.

## 8. 학습자 사용 시나리오 (요약)

1. 저장소를 받는다 → 루트 `README.md`를 따라 `uv venv` + `uv sync`.
2. `00_setup`에서 Hello World로 실행 체인을 확인.
3. 폴더 번호 순서대로 `README.md` → `NN_topic.py`를 정독·실행 → `exercises/` 풀이 → `solutions/`와 비교.
4. Phase 4 진입 시 그 Phase의 의존성 그룹을 추가 설치.
5. (옵션) `17_capstone`으로 미니 프로젝트.

## 9. 성공 기준

- 각 학습 스크립트는 추가 인자 없이 `uv run python <path>`로 즉시 실행 가능하고 의미 있는 출력이 나온다.
- 각 연습문제는 정답을 채우면 'OK'가 출력되고, 비워두면 의미 있는 assert 실패를 낸다.
- 폴더별 README만 따라가도 학습자가 막힘 없이 학습을 진행할 수 있다.
- 다른 언어 경험자가 처음부터 끝까지 진행했을 때, 파이썬 공식 문서를 무리 없이 읽을 수 있는 수준이 된다.
