# Python Tutorial — Phase 4 (실전 라이브러리) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development.

**Goal:** Phase 4 다섯 폴더(`12_testing`, `13_data_science`, `14_web_backend`, `15_automation`, `16_tooling_packaging`)에 학습 콘텐츠 채우기. 각 폴더 진입 시 해당 optional-dependencies 그룹 설치.

**Tech Stack 추가**: pytest, numpy, pandas, matplotlib, fastapi+TestClient, pydantic, requests, beautifulsoup4, click, ruff, black, mypy.

**참조:** 스펙, Phase 0~3 완료 (다섯 polders와 mypy/uv.lock 모두 commit 됨).

---

## 스타일 규칙

- 학습 스크립트: 표준 (docstring + 구분선 + 한국어 주석 + 데모 블록).
- **타입 힌트 사용 가능** (Phase 3 이후).
- **외부 라이브러리 사용 가능** — 폴더별 그룹.
- **모든 IO는 임시 자원** (tempfile)에서. 저장소 잔여 파일 금지.

연습문제·정답: 기본 패턴은 TODO + assert + `print("OK")`. **단, 12_testing 만 pytest 컨벤션 (`test_*.py`)을 따른다.** README 에 그 차이 명시.

---

## Task 1: `12_testing/` — 테스트 (pytest)

### 사전 설치
실행자가 `uv pip install -e ".[test]"` 로 pytest, pytest-cov 설치.

### 학습 스크립트 (5)
모든 학습 스크립트는 단독 실행 가능 (`uv run python ...`). `unittest` 도 짧게 다룬다.

**`01_unittest_basics.py`** — unittest (표준 라이브러리)
- `import unittest`
- `class TestX(unittest.TestCase): def test_y(self): self.assertEqual(...)`
- `unittest.main()` 직접 실행
- 어셋션 메서드 종류 한 줄씩 (assertEqual, assertTrue, assertIn, assertRaises)
- Demo: 작은 TestCase 정의 후 unittest.main(exit=False) 으로 실행

**`02_pytest_basics.py`** — pytest 입문
- `def test_xxx():` 함수만 있으면 됨 (클래스 불필요)
- assert 문 그대로 (`assert a == b`)
- 실패 시 자세한 메시지 자동 (pytest 의 장점)
- 파일/함수 이름이 `test_` 로 시작해야 자동 수집
- Demo: 학습용 스크립트라 직접 pytest 호출 — `pytest.main(["-x", __file__])` 한 줄

**`03_fixtures.py`** — pytest 픽스처
- `@pytest.fixture` 데코레이터로 픽스처 정의
- 테스트 함수의 인자로 받음 (이름 매칭)
- scope: function (기본), module, session
- yield 픽스처로 setup/teardown (tempfile 같은)
- Demo: 픽스처 2개 만들고 사용하는 테스트 정의, pytest.main 으로 실행

**`04_mocking.py`** — 모킹
- `from unittest.mock import MagicMock, patch`
- `MagicMock()` — 어떤 속성·메서드 호출도 받아줌
- `with patch("모듈.대상") as m:` 으로 일시적 교체
- `m.return_value = ...` 로 반환값 지정, `m.assert_called_with(...)` 로 호출 검증
- Demo: 내부 함수 mock 으로 교체해 테스트

**`05_parametrize.py`** — 매개변수화 테스트
- `@pytest.mark.parametrize("a,b,expected", [(1,1,2), (2,3,5)])`
- 한 테스트 함수가 여러 입력으로 실행
- 출력에 어떤 입력으로 실패했는지 보임
- Demo: parametrize 적용한 add 테스트, pytest.main 으로 실행

### Exercises (5) — `test_NN_*.py` 형식

**여기서는 OK 패턴이 아닌 pytest 네이티브 형식 사용.** 각 파일에는 TODO 가 들어있고 pytest 가 함수를 자동 수집·실행.

- `exercises/test_01_unittest.py`: TestCase 안에 `test_add_works` 같은 메서드 한 두 개 TODO.
- `exercises/test_02_pytest.py`: `def test_*():` 함수 TODO (assert 비어있음).
- `exercises/test_03_fixtures.py`: 픽스처 + 테스트 TODO.
- `exercises/test_04_mocking.py`: patch / MagicMock 사용 TODO.
- `exercises/test_05_parametrize.py`: `@pytest.mark.parametrize` 사용 TODO.

### Solutions (5)

`solutions/test_NN_*.py` — pytest 가 통과해야 한다.

### README

```
# 12_testing — 테스트 (pytest)

## 사전 준비
[bash fence]
uv pip install -e ".[test]"
[/bash fence]

## 배우는 것
- unittest 기본 (표준 라이브러리)
- pytest 입문 — test_ 자동 수집 + 평범한 assert
- 픽스처 (@pytest.fixture, scope, yield)
- 모킹 (unittest.mock + patch)
- 매개변수화 (@pytest.mark.parametrize)

## 학습 순서
1. `01_unittest_basics.py`
2. `02_pytest_basics.py`
3. `03_fixtures.py`
4. `04_mocking.py`
5. `05_parametrize.py`

## 실행 방법
학습 스크립트는 평소처럼:
[bash fence]
uv run python 12_testing/02_pytest_basics.py
[/bash fence]

## 연습문제 (pytest 컨벤션)
이 폴더만 연습문제가 OK 패턴 대신 pytest 의 `test_*.py` 형식을 따른다:
[bash fence]
uv run pytest 12_testing/exercises/ -q
uv run pytest 12_testing/solutions/ -q
[/bash fence]
- 미완성 연습은 일부 테스트가 실패한다.
- 풀이를 채우면 모두 통과한다.
- `solutions/` 와 비교.
```
(실제 `[bash fence]` 는 ```bash 펜스)

### Steps

1. `uv pip install -e ".[test]"`
2. `mkdir -p 12_testing/exercises 12_testing/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7. 학습 무오류 검증
8. **정답 pytest 통과**: `uv run pytest 12_testing/solutions/ -q` → 모두 PASS
9. **빈 exercise pytest 일부 실패**: `uv run pytest 12_testing/exercises/ -q` → FAIL (의도된 미구현)
10. 커밋:
    ```
    git add 12_testing/ pyproject.toml uv.lock
    git commit -m "feat(12_testing): unittest/pytest/fixtures/mocking/parametrize — 학습 5 + 연습 5 + 정답 5"
    ```

---

## Task 2: `13_data_science/` — 데이터 분석

### 사전 설치
`uv pip install -e ".[data]"` → numpy, pandas, matplotlib, jupyter.

### 학습 스크립트 (5)

모두 `.py` 사용 (스펙에서 ipynb 허용했지만 검증·일관성 위해 `.py` 통일).
matplotlib 은 `matplotlib.use("Agg")` 로 헤드리스 모드 후 `savefig` 로 임시 디렉터리에 저장.

**`01_numpy_basics.py`** — numpy
- `import numpy as np`
- `np.array([1,2,3])`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
- shape, dtype, reshape
- 벡터화 연산: `a + b`, `a * 2`, `np.sqrt(a)` (Python loop 보다 빠름)
- 인덱싱·슬라이싱·불리언 마스킹
- Demo: 1D/2D 배열 만들고 연산

**`02_numpy_advanced.py`** — numpy 심화
- 브로드캐스팅 규칙 한 그림 설명 (주석으로)
- aggregations: `sum`, `mean`, `std`, `min`, `max`, `argmin`, `argmax`
- axis 매개변수
- 행렬 곱 `@`, `np.dot`
- random: `np.random.default_rng(seed=42)` 사용
- Demo: 2D 데이터에 axis 별 집계, 행렬 곱

**`03_pandas_series_dataframe.py`** — pandas 기본
- `import pandas as pd`
- `pd.Series([1,2,3], index=["a","b","c"])`
- `pd.DataFrame({"col1": [...], "col2": [...]})`
- 인덱싱: `.loc[행, 열]`, `.iloc[행번호, 열번호]`
- 열 추가/수정, dtype
- Demo: 작은 DataFrame 만들어 조작

**`04_pandas_io_filter_groupby.py`** — pandas IO/필터/그룹핑
- CSV 읽기 (tempfile 사용): `pd.read_csv(path)`, `to_csv(path)`
- 필터: `df[df["col"] > 0]`
- 정렬: `sort_values`
- groupby + agg: `df.groupby("category")["value"].sum()`
- Demo: 임시 CSV 만들어 읽고 필터/그룹

**`05_matplotlib_intro.py`** — matplotlib
- 헤드리스: `import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt`
- `plt.plot(x, y)`, `plt.bar(...)`, `plt.scatter(...)`
- `plt.title`, `xlabel`, `ylabel`
- `plt.savefig(임시경로)` 후 파일 존재 확인
- Demo: 간단한 라인 차트를 임시 PNG 로 저장하고 path/size 출력

### Exercises (5)

표준 OK 패턴.

- `ex01_numpy_basics`: 1~10 배열 만들고 평균/표준편차/최대값 계산. assert.
- `ex02_numpy_advanced`: 2D 배열 (3x4) 만들고 행/열 합 계산. assert.
- `ex03_pandas_series_dataframe`: DataFrame 만들고 특정 열 평균. assert.
- `ex04_pandas_io_filter_groupby`: tempfile CSV 만들고 read → groupby → agg 결과 검증.
- `ex05_matplotlib_intro`: 임시 PNG 에 저장 후 파일 size > 0 assert.

### Solutions (5)

같은 파일명, "OK" 출력.

### README

```
# 13_data_science — 데이터 분석 (numpy / pandas / matplotlib)

## 사전 준비
[bash] uv pip install -e ".[data]" [/bash]

## 배우는 것
- numpy: 배열·벡터화 연산·브로드캐스팅·집계
- pandas: Series / DataFrame, IO, 필터, groupby
- matplotlib: 헤드리스 모드 (Agg) + savefig

## 학습 순서
1. `01_numpy_basics.py`
2. `02_numpy_advanced.py`
3. `03_pandas_series_dataframe.py`
4. `04_pandas_io_filter_groupby.py`
5. `05_matplotlib_intro.py`

## 실행 방법
[bash] uv run python 13_data_science/01_numpy_basics.py [/bash]

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO 채우기.
```

### Steps

1. `uv pip install -e ".[data]"`
2. `mkdir -p 13_data_science/exercises 13_data_science/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7-9. 표준 검증
10. 커밋:
    ```
    git add 13_data_science/ pyproject.toml uv.lock
    git commit -m "feat(13_data_science): numpy/pandas/matplotlib — 학습 5 + 연습 5 + 정답 5"
    ```

---

## Task 3: `14_web_backend/` — 웹 백엔드

### 사전 설치
`uv pip install -e ".[web]"` → fastapi, uvicorn, requests, pydantic, sqlalchemy.

### 학습 스크립트 (5)

**`01_requests_client.py`** — requests
- `import requests`
- `r = requests.get("https://httpbin.org/get")`, `r.json()`, `r.status_code`
- **실제 네트워크 호출 X** — `unittest.mock.patch` 로 응답을 모킹
- 또는 FastAPI TestClient 와 연계 가능 (다음 파일에서)
- 데모: mock 한 응답으로 GET/POST 패턴 시연

**`02_pydantic_models.py`** — pydantic
- `from pydantic import BaseModel, Field, ValidationError`
- `class User(BaseModel): name: str; age: int = Field(ge=0)`
- 직렬화: `user.model_dump()`, `user.model_dump_json()`
- 역직렬화: `User.model_validate(dict)`, `User.model_validate_json(s)`
- 유효성 실패 시 ValidationError
- Demo: 정상/잘못된 데이터 검증

**`03_fastapi_intro.py`** — FastAPI
- `from fastapi import FastAPI`
- `app = FastAPI()`
- `@app.get("/")`, `@app.post("/items")`
- pydantic 모델로 자동 검증
- **TestClient 로 검증** (실제 서버 띄우지 않음):
  - `from fastapi.testclient import TestClient`
  - `client = TestClient(app)`
  - `r = client.get("/")`
- Demo: 라우트 3~4개 + TestClient 로 호출

**`04_fastapi_path_query.py`** — Path/Query/Body
- `@app.get("/items/{id}")` 경로 파라미터
- 함수 시그니처에 `id: int` 자동 캐스팅
- 쿼리: `def get(q: str = "")` 기본값
- Body: pydantic 모델로 받기
- 자동 OpenAPI 문서 한 줄 언급
- Demo: 경로/쿼리/바디 각각 + TestClient

**`05_sqlalchemy_basics.py`** — SQLAlchemy (간단)
- `from sqlalchemy import create_engine, Column, Integer, String, select`
- `from sqlalchemy.orm import declarative_base, Session`
- in-memory SQLite: `create_engine("sqlite:///:memory:")`
- 모델 정의 → 테이블 생성 → 삽입 → 조회
- Demo: User 모델 만들고 in-memory DB 에 3행 넣고 조회

### Exercises (5)

표준 OK 패턴.

- `ex01_requests_client`: mock 으로 가짜 응답 만들고 `client.get` 호출, status_code/JSON 키 검증.
- `ex02_pydantic_models`: `Book(BaseModel)` (title, pages: ge=0) 정의 + 잘못된 데이터로 ValidationError 발생 확인.
- `ex03_fastapi_intro`: 작은 FastAPI 앱 + TestClient 로 GET 호출 → 응답 검증.
- `ex04_fastapi_path_query`: 경로 파라미터 + 쿼리 함수 작성 + TestClient 호출.
- `ex05_sqlalchemy_basics`: in-memory DB, User 삽입 후 조회 결과 길이 확인.

### Solutions (5)

### README

```
# 14_web_backend — 웹 백엔드

## 사전 준비
[bash] uv pip install -e ".[web]" [/bash]

## 배우는 것
- requests (mock 응답으로 GET/POST 시연)
- pydantic (모델 검증, 직렬화)
- FastAPI (TestClient 로 실제 서버 없이 검증)
- 경로/쿼리/바디 매개변수
- SQLAlchemy in-memory SQLite 맛보기

## 학습 순서
1. `01_requests_client.py`
2. `02_pydantic_models.py`
3. `03_fastapi_intro.py`
4. `04_fastapi_path_query.py`
5. `05_sqlalchemy_basics.py`

## 실행 방법
[bash] uv run python 14_web_backend/03_fastapi_intro.py [/bash]

## 연습문제
- 모든 검증은 TestClient/in-memory DB/mock 으로 — 외부 네트워크·디스크 X.
```

### Steps

1. `uv pip install -e ".[web]"`
2. `mkdir -p 14_web_backend/exercises 14_web_backend/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7-9. 표준 검증
10. 커밋:
    ```
    git add 14_web_backend/ pyproject.toml uv.lock
    git commit -m "feat(14_web_backend): requests/pydantic/FastAPI(TestClient)/SQLAlchemy — 학습 5 + 연습 5 + 정답 5"
    ```

---

## Task 4: `15_automation/` — 자동화·스크립팅

### 사전 설치
`uv pip install -e ".[auto]"` → beautifulsoup4, click.

### 학습 스크립트 (5)

**`01_argparse_cli.py`** — argparse
- 표준 라이브러리 CLI
- `parser = argparse.ArgumentParser(description="...")` 
- `parser.add_argument("--name", default="World")`
- `args = parser.parse_args(["--name", "Kee"])` (직접 인자 리스트 전달로 테스트 가능)
- Demo: 간단 CLI 흉내

**`02_click_cli.py`** — click (외부 라이브러리)
- `import click`
- `@click.command() @click.option("--name", default="World") def hello(name): ...`
- argparse 보다 데코레이터 기반으로 간결
- Demo: click.Command 만들고 `runner.invoke()` 로 테스트
- `from click.testing import CliRunner`

**`03_subprocess.py`** — subprocess
- `subprocess.run(["echo", "hi"], capture_output=True, text=True)`
- `.stdout`, `.stderr`, `.returncode`
- `check=True` 로 실패 시 예외
- `shell=False` 권장 (인젝션 위험)
- Demo: `ls -la` (또는 OS 독립적인 `python --version`) 실행 후 결과 출력

**`04_beautifulsoup.py`** — BeautifulSoup HTML 파싱
- `from bs4 import BeautifulSoup`
- HTML 문자열 파싱 — **로컬 문자열 사용 (네트워크 X)**
- `soup.find("a")`, `soup.find_all("li", class_="x")`
- `.get_text()`, `.attrs["href"]`
- Demo: 내장 HTML 문자열에서 모든 링크 추출

**`05_os_pathlib_automation.py`** — 파일/디렉터리 자동화
- pathlib 의 글로빙 (`Path.glob`, `Path.rglob`)
- `shutil.copy`, `shutil.move`, `shutil.rmtree` (한 줄씩)
- tempfile.TemporaryDirectory 안에서 디렉터리 트리 생성·조작
- Demo: 임시 디렉터리에 파일 3개 만들고 .txt 만 골라 처리

### Exercises (5)

표준 OK.

- `ex01_argparse_cli`: parser 만들고 `parser.parse_args(["--name", "Kee"])` 후 namespace 검증.
- `ex02_click_cli`: click command + CliRunner 로 invoke 후 stdout 검증.
- `ex03_subprocess`: `subprocess.run(["python", "-c", "print('hi')"], ...)` 후 stdout 검증.
- `ex04_beautifulsoup`: 주어진 HTML 문자열에서 모든 `<a>` 의 href 추출, list 검증.
- `ex05_os_pathlib_automation`: TemporaryDirectory 안에 .txt 3개, .log 1개 만들고 .txt 만 리스트로 추출.

### Solutions (5)

### README

```
# 15_automation — 자동화·스크립팅

## 사전 준비
[bash] uv pip install -e ".[auto]" [/bash]

## 배우는 것
- argparse / click 으로 CLI 만들기
- subprocess 로 외부 명령 실행 (안전한 사용)
- BeautifulSoup 로 HTML 파싱 (로컬 문자열로 시연)
- pathlib + shutil 로 파일/디렉터리 자동화

## 학습 순서
1. `01_argparse_cli.py`
2. `02_click_cli.py`
3. `03_subprocess.py`
4. `04_beautifulsoup.py`
5. `05_os_pathlib_automation.py`

## 실행 방법
[bash] uv run python 15_automation/01_argparse_cli.py [/bash]

## 연습문제
- 모든 IO 는 임시 자원 + 로컬 문자열 — 외부 네트워크 X.
```

### Steps

1. `uv pip install -e ".[auto]"`
2. `mkdir -p 15_automation/exercises 15_automation/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7-9. 표준 검증
10. 커밋:
    ```
    git add 15_automation/ pyproject.toml uv.lock
    git commit -m "feat(15_automation): argparse/click/subprocess/BeautifulSoup/pathlib — 학습 5 + 연습 5 + 정답 5"
    ```

---

## Task 5: `16_tooling_packaging/` — 툴링·패키징

### 사전 설치
`uv pip install -e ".[dev]"` → ruff, black.

### 학습 스크립트 (5)

**`01_ruff_lint.py`** — ruff 린트
- 빠른 린트 — flake8 등을 대체
- `pyproject.toml` 에 `[tool.ruff]` 설정 가능 (실제 설정은 이 폴더에서 보여주지 않고, 명령 시연만)
- Demo: print 로 `uv run ruff check 16_tooling_packaging/` 사용법 안내
- 의도된 nit 가 있는 코드 한 줄 (또는 깨끗한 코드만, ruff 통과 보장)

**`02_black_format.py`** — black 포매팅
- 의견 강한 포매터 — 설정 거의 없음
- Demo: `uv run black 16_tooling_packaging/02_black_format.py --check`
- 깨끗한 코드 유지 (black 통과)

**`03_mypy_recap.py`** — mypy 재방문
- 10_typing 에서 다룸을 한 줄 언급
- 프로젝트 단위 mypy 사용법: `uv run mypy <폴더>`
- `pyproject.toml` 에 mypy 설정 위치 (실제 적용은 하지 않음)
- Demo: 작은 타입 정확한 함수

**`04_pyproject_anatomy.py`** — pyproject.toml 해부
- 실제 코드 X — 주석으로 pyproject.toml 의 각 섹션 설명
- `[project]`, `[project.optional-dependencies]`, `[build-system]`, `[tool.ruff]`, `[tool.black]`, `[tool.mypy]`
- Demo: print 로 각 섹션의 역할 표 형식 출력

**`05_packaging_with_uv.py`** — uv 로 패키지 만들기
- uv build 명령 한 줄
- 휠 파일이 무엇인지 한 줄
- PyPI 업로드는 uv publish (한 줄 언급)
- Demo: print 로 단계 안내 (실제 uv build 는 학습자 수동)

### Exercises (5)

표준 OK.

- `ex01_ruff_lint`: 깨끗한 작은 함수 작성 + assert (ruff 가 통과하는지는 추가 검증 항목).
- `ex02_black_format`: 의도적으로 포맷 흐트러진 코드를 정답에선 black 적용한 상태로.
- `ex03_mypy_recap`: 타입 힌트 있는 함수 + assert.
- `ex04_pyproject_anatomy`: 주어진 pyproject.toml 일부 문자열에서 특정 그룹 의존성 추출하는 함수 (tomllib 사용).
- `ex05_packaging_with_uv`: 가짜 pyproject.toml 일부 dict 만들고 검증.

### Solutions (5)

### README

```
# 16_tooling_packaging — 툴링·패키징

## 사전 준비
[bash] uv pip install -e ".[dev]" [/bash]

## 배우는 것
- ruff — 빠른 린트
- black — 의견 강한 포매터
- mypy — 정적 타입 검사 (10_typing 재방문)
- pyproject.toml 해부
- uv build / publish — 배포 흐름 맛보기

## 학습 순서
1. `01_ruff_lint.py`
2. `02_black_format.py`
3. `03_mypy_recap.py`
4. `04_pyproject_anatomy.py`
5. `05_packaging_with_uv.py`

## 실행 방법
[bash] uv run python 16_tooling_packaging/01_ruff_lint.py [/bash]

## 도구 사용
[bash]
uv run ruff check 16_tooling_packaging/
uv run black --check 16_tooling_packaging/
uv run mypy 16_tooling_packaging/
[/bash]

## 연습문제
- exercises/ex01_*.py ~ ex05_*.py TODO 채우기.
```

### Steps

1. `uv pip install -e ".[dev]"`
2. `mkdir -p 16_tooling_packaging/exercises 16_tooling_packaging/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7-9. 표준 검증
10. 커밋:
    ```
    git add 16_tooling_packaging/ pyproject.toml uv.lock
    git commit -m "feat(16_tooling_packaging): ruff/black/mypy/pyproject/uv build — 학습 5 + 연습 5 + 정답 5"
    ```

---

## Phase 4 종합 검증 (모든 Task 후)

```bash
for d in 12_testing 13_data_science 14_web_backend 15_automation 16_tooling_packaging; do
  echo "=== $d 학습 ==="
  for f in $d/0[1-9]_*.py; do
    uv run python "$f" >/dev/null 2>&1 && echo "OK $f" || echo "FAIL $f"
  done
done

# 12_testing 은 pytest 컨벤션
uv run pytest 12_testing/solutions/ -q

# 나머지 폴더 정답
for d in 13_data_science 14_web_backend 15_automation 16_tooling_packaging; do
  echo "=== $d 정답 ==="
  for f in $d/solutions/ex*.py; do
    out=$(uv run python "$f" 2>&1 | tail -1)
    [ "$out" = "OK" ] && echo "PASS $f" || echo "FAIL $f -> $out"
  done
done
```

---

## 다음 Phase 안내

Phase 4 완료 후 Phase 5 (`17_capstone`) 미니 프로젝트 계획서 — 선택 사항.
