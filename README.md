# Python Tutorial — 단계별 파이썬 학습

다른 언어 경험은 있지만 파이썬이 처음인 학습자를 위해, **기초 자료형 → 자료구조 → 함수 → 객체지향 → 고급 → 동시성 → 실전 라이브러리**까지 한 줄 한 줄 주석과 함께 정리한 학습 저장소다.

## 학습 전 준비

### 1) `uv` 설치
이 저장소는 `uv`로 파이썬 버전·가상환경·패키지를 한 번에 관리한다.

macOS:
```bash
brew install uv
```

Linux/WSL:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 버전 확인:
```bash
uv --version
```

### 2) 가상환경과 의존성
저장소 루트에서 다음을 한 번 실행한다:
```bash
uv sync
```
`.python-version`에 따라 Python 3.12가 자동으로 설치되고 `.venv/`가 생성된다.

### 3) 첫 실행 확인
```bash
uv run python 00_setup/01_hello.py
```
"안녕, 파이썬!" 비슷한 출력이 나오면 준비 완료다.

## 학습 순서

번호 순서대로 폴더를 진행한다. 각 폴더 안의 `README.md`를 먼저 읽고, `NN_topic.py`를 순서대로 실행해본 뒤, `exercises/`의 TODO를 채워본다.

### Phase 1 — 기초
- `01_basics/` — 변수, 자료형, 제어흐름
- `02_data_structures/` — list, tuple, dict, set, 컴프리헨션
- `03_functions/` — 함수, *args/**kwargs, lambda, 클로저
- `04_modules_packages/` — import, 표준 라이브러리

### Phase 2 — 중급
- `05_oop/` — 클래스, 상속, 매직 메서드, dataclass
- `06_errors_exceptions/` — 예외 처리, EAFP
- `07_io_files/` — 파일 IO, JSON, CSV, with
- `08_iterators_generators/` — yield, itertools

### Phase 3 — 고급
- `09_advanced_python/` — 데코레이터, 컨텍스트 매니저, descriptor
- `10_typing/` — 타입 힌트, mypy
- `11_concurrency/` — threading, multiprocessing, asyncio

### Phase 4 — 실전 라이브러리
- `12_testing/` — pytest, fixture, mocking
- `13_data_science/` — numpy, pandas, matplotlib
- `14_web_backend/` — requests, FastAPI, pydantic
- `15_automation/` — argparse, BeautifulSoup, subprocess
- `16_tooling_packaging/` — ruff, black, mypy, uv 배포

### Phase 5 (옵션)
- `17_capstone/` — 미니 프로젝트

## 파일 형식 약속

- 학습용 `.py`는 모두 단독 실행 가능:
  ```bash
  uv run python 02_data_structures/01_list.py
  ```
- 주석은 한국어. 식별자(변수·함수명)는 영어.
- 각 폴더에 `exercises/`(TODO) + `solutions/`(정답)이 들어 있다.

## 파일별 의존성 설치

Phase 4 이전까지는 추가 설치 없이 돌아간다. 그 이후엔 폴더에 진입할 때마다:

```bash
uv pip install -e ".[test]"      # 12_testing
uv pip install -e ".[typing]"    # 10_typing
uv pip install -e ".[data]"      # 13_data_science
uv pip install -e ".[web]"       # 14_web_backend
uv pip install -e ".[auto]"      # 15_automation
uv pip install -e ".[dev]"       # 16_tooling_packaging
```

각 그룹이 어떤 라이브러리를 포함하는지는 `pyproject.toml`을 참고한다.
