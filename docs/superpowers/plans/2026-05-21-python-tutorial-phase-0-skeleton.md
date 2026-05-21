# Python Tutorial — Phase 0 (골격 구축) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 학습용 파이썬 튜토리얼 저장소의 **골격**을 만든다 — 루트 설정 파일, 18개 학습 폴더의 빈 껍데기, 그리고 `00_setup`의 실제 학습 콘텐츠까지. 실행하면 `uv` 환경이 잘 잡혀 있고 `00_setup`의 hello world가 실제로 돌아간다.

**Architecture:** 루트에 `pyproject.toml` + `.python-version` + `README.md`로 환경/안내를 잡고, 18개 학습 폴더는 4단 README 템플릿을 따른 placeholder README만 둔다. `00_setup`만은 Phase 0에서 실제 콘텐츠를 채워, 학습자가 첫 단원을 곧바로 돌릴 수 있게 한다. 검증은 `uv sync` 성공 + `00_setup/01_hello.py` 실행 결과 확인으로 끝낸다.

**Tech Stack:** Python 3.12, uv (가상환경·패키지 관리), 표준 라이브러리만 사용.

**참조 스펙:** `docs/superpowers/specs/2026-05-21-python-tutorial-design.md`

---

## File Structure (Phase 0에서 생성/수정되는 파일 전체)

생성 파일:
- `pyproject.toml` — uv 프로젝트 메타데이터 + 의존성 그룹
- `.python-version` — 파이썬 3.12 고정
- `.gitignore` — `.venv/`, `__pycache__/`, `.ipynb_checkpoints/` 등 무시
- `README.md` — 저장소 루트 안내 (전체 학습 가이드)
- `00_setup/README.md` — 환경 세팅 안내
- `00_setup/01_hello.py` — 가장 단순한 실행 예제
- `00_setup/02_about_uv.py` — uv 명령어 소개 (주석으로)
- `01_basics/README.md` ~ `17_capstone/README.md` — 학습 폴더 placeholder (총 17개)

생성 디렉토리 (Phase 0에서는 빈 폴더만; 내용은 각 Phase에서 채움):
- `00_setup/` ~ `17_capstone/` (총 18개)

수정 파일: 없음 (백지 상태에서 시작)

각 파일은 한 가지 책임만 진다:
- `pyproject.toml`: 의존성 선언만 (코드 없음)
- `README.md`(루트): 학습 가이드 안내만
- `00_setup/01_hello.py`: 첫 실행 체험만
- 각 폴더 `README.md`: 그 폴더 학습 안내만

---

## Task 1: uv 설치 확인과 작업 디렉토리 진입

**Files:** 없음 (확인만)

- [ ] **Step 1: uv가 설치돼 있는지 확인**

Run:
```bash
uv --version
```
Expected: `uv 0.4.x` 또는 그 이상이 출력. 출력이 안 나오면 [uv 공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/)를 보고 설치한다 (macOS: `brew install uv`).

- [ ] **Step 2: 작업 디렉토리로 진입**

Run:
```bash
cd /Users/keesoonpark/Workspace/python-tutorial
pwd
ls -la
```
Expected: `pwd`가 `python-tutorial`이고, 현재는 `docs/`와 `.omc/`만 있다.

---

## Task 2: 루트 설정 파일 생성 (`.python-version`, `.gitignore`)

**Files:**
- Create: `.python-version`
- Create: `.gitignore`

- [ ] **Step 1: `.python-version` 생성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/.python-version`

내용 (한 줄):
```
3.12
```

- [ ] **Step 2: `.gitignore` 생성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/.gitignore`

내용:
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# uv / venv
.venv/
.python-version.local

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
.idea/

# 빌드
*.egg-info/
dist/
build/
```

- [ ] **Step 3: 두 파일이 생성됐는지 확인**

Run:
```bash
ls -la .python-version .gitignore
cat .python-version
```
Expected: 두 파일이 보이고, `.python-version`은 `3.12` 한 줄.

---

## Task 3: `pyproject.toml` 생성

**Files:**
- Create: `pyproject.toml`

- [ ] **Step 1: `pyproject.toml` 작성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/pyproject.toml`

내용:
```toml
[project]
name = "python-tutorial"
version = "0.1.0"
description = "단계별 파이썬 학습 자료 (기초 → 중급 → 고급 → 실전 라이브러리)"
requires-python = ">=3.12"
dependencies = []  # Phase 1~3은 표준 라이브러리만 사용한다.

# Phase별 라이브러리는 optional-dependencies로 분리한다.
# 해당 Phase에 진입할 때 `uv pip install -e ".[<group>]"` 로 설치한다.
[project.optional-dependencies]
data    = ["numpy", "pandas", "matplotlib", "jupyter"]                    # 13_data_science
web     = ["fastapi", "uvicorn", "requests", "pydantic", "sqlalchemy"]    # 14_web_backend
auto    = ["beautifulsoup4", "click"]                                     # 15_automation
test    = ["pytest", "pytest-cov"]                                        # 12_testing
typing  = ["mypy"]                                                        # 10_typing
dev     = ["ruff", "black"]                                               # 16_tooling_packaging

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
# 학습용 저장소이므로 빌드할 패키지는 없다.
# hatch는 메타데이터만 필요해서 단순히 가짜 패키지 디렉토리 하나만 가리키게 한다.
bypass-selection = true
```

- [ ] **Step 2: `uv sync`로 환경을 실제로 만든다**

Run:
```bash
uv sync
```
Expected:
- `.venv/` 디렉토리가 생성된다.
- "Resolved 0 packages" 또는 "Installed 0 packages" 비슷한 메시지가 나오고 에러 없이 끝난다 (의존성이 비어 있으므로).

만약 hatch 빌드 단계에서 에러가 난다면 `[tool.hatch.build.targets.wheel] bypass-selection = true` 줄 대신 다음을 시도한다:
```toml
[tool.hatch.build.targets.wheel]
packages = []
```

- [ ] **Step 3: 가상환경 확인**

Run:
```bash
ls .venv/bin/python
uv run python --version
```
Expected:
- `.venv/bin/python` 존재
- `Python 3.12.x` 출력

---

## Task 4: 루트 `README.md` 생성

**Files:**
- Create: `README.md`

- [ ] **Step 1: 루트 README 작성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/README.md`

내용:
```markdown
# Python Tutorial — 단계별 파이썬 학습

다른 언어 경험은 있지만 파이썬이 처음인 학습자를 위해, **기초 자료형 → 자료구조 → 함수 → 객체지향 → 고급 → 동시성 → 실전 라이브러리**까지 한 줄 한 줄 주석과 함께 정리한 학습 저장소다.

## 학습 전 준비

### 1) `uv` 설치
이 저장소는 `uv`로 파이썬 버전·가상환경·패키지를 한 번에 관리한다.

macOS:
\`\`\`bash
brew install uv
\`\`\`

Linux/WSL:
\`\`\`bash
curl -LsSf https://astral.sh/uv/install.sh | sh
\`\`\`

설치 후 버전 확인:
\`\`\`bash
uv --version
\`\`\`

### 2) 가상환경과 의존성
저장소 루트에서 다음을 한 번 실행한다:
\`\`\`bash
uv sync
\`\`\`
`.python-version`에 따라 Python 3.12가 자동으로 설치되고 `.venv/`가 생성된다.

### 3) 첫 실행 확인
\`\`\`bash
uv run python 00_setup/01_hello.py
\`\`\`
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
  \`\`\`bash
  uv run python 02_data_structures/01_list.py
  \`\`\`
- 주석은 한국어. 식별자(변수·함수명)는 영어.
- 각 폴더에 `exercises/`(TODO) + `solutions/`(정답)이 들어 있다.

## 파일별 의존성 설치

Phase 4 이전까지는 추가 설치 없이 돌아간다. 그 이후엔 폴더에 진입할 때마다:

\`\`\`bash
uv pip install -e ".[test]"      # 12_testing
uv pip install -e ".[typing]"    # 10_typing
uv pip install -e ".[data]"      # 13_data_science
uv pip install -e ".[web]"       # 14_web_backend
uv pip install -e ".[auto]"      # 15_automation
uv pip install -e ".[dev]"       # 16_tooling_packaging
\`\`\`

각 그룹이 어떤 라이브러리를 포함하는지는 `pyproject.toml`을 참고한다.
```

- [ ] **Step 2: README 확인**

Run:
```bash
head -20 README.md
```
Expected: "# Python Tutorial — 단계별 파이썬 학습" 으로 시작.

---

## Task 5: 17개 학습 폴더 + placeholder README 생성

각 폴더는 4단(배우는 것 / 학습 순서 / 실행 방법 / 연습문제) 템플릿을 따른 placeholder README를 갖는다. 내용은 비어 있지만 구조는 처음부터 통일.

**Files:**
- Create: `01_basics/README.md` ~ `17_capstone/README.md` (총 17개)
- Create directories: `01_basics/` ~ `17_capstone/`

- [ ] **Step 1: 17개 폴더 한 번에 생성**

Run:
```bash
mkdir -p 01_basics 02_data_structures 03_functions 04_modules_packages \
         05_oop 06_errors_exceptions 07_io_files 08_iterators_generators \
         09_advanced_python 10_typing 11_concurrency \
         12_testing 13_data_science 14_web_backend 15_automation 16_tooling_packaging \
         17_capstone
ls -d */ | grep -v -E '(docs|\.omc|\.venv)'
```
Expected: 17개 폴더가 출력된다 (00_setup 제외 — 다음 Task에서 생성).

- [ ] **Step 2: README 템플릿 함수 준비**

각 폴더 README는 다음 형태를 따른다. (Step 3에서 17번 반복 작성)

```markdown
# {NN_folder_name} — {한국어 제목}

> 이 폴더는 **{Phase N}**에서 채워질 예정입니다. (현재는 placeholder)

## 배우는 것
- (Phase N에서 채워짐)

## 학습 순서
1. (Phase N에서 채워짐)

## 실행 방법
\`\`\`bash
uv run python {NN_folder}/01_*.py
\`\`\`

## 연습문제
- `exercises/` 의 TODO를 채우고, `solutions/` 와 비교한다.
- (Phase N에서 채워짐)
```

- [ ] **Step 3: 17개 README 작성**

각 폴더에 대해 아래 값을 채워 `<folder>/README.md`를 만든다. 매핑:

| 폴더 | 한국어 제목 | Phase |
|------|------------|-------|
| 01_basics | 기초 자료형과 제어흐름 | Phase 1 |
| 02_data_structures | 자료구조 | Phase 1 |
| 03_functions | 함수 | Phase 1 |
| 04_modules_packages | 모듈과 패키지 | Phase 1 |
| 05_oop | 객체지향 프로그래밍 | Phase 2 |
| 06_errors_exceptions | 예외 처리 | Phase 2 |
| 07_io_files | 파일 입출력 | Phase 2 |
| 08_iterators_generators | 이터레이터와 제너레이터 | Phase 2 |
| 09_advanced_python | 데코레이터·컨텍스트·디스크립터 | Phase 3 |
| 10_typing | 타입 힌트 | Phase 3 |
| 11_concurrency | 동시성 (threading/multiprocessing/asyncio) | Phase 3 |
| 12_testing | 테스트 (pytest) | Phase 4 |
| 13_data_science | 데이터 분석 (numpy/pandas/matplotlib) | Phase 4 |
| 14_web_backend | 웹 백엔드 (FastAPI/requests) | Phase 4 |
| 15_automation | 자동화·스크립팅 | Phase 4 |
| 16_tooling_packaging | 툴링·패키징 | Phase 4 |
| 17_capstone | 미니 프로젝트 (옵션) | Phase 5 |

각 파일 내용 예시 (`01_basics/README.md`):
```markdown
# 01_basics — 기초 자료형과 제어흐름

> 이 폴더는 **Phase 1**에서 채워질 예정입니다. (현재는 placeholder)

## 배우는 것
- (Phase 1에서 채워짐)

## 학습 순서
1. (Phase 1에서 채워짐)

## 실행 방법
\`\`\`bash
uv run python 01_basics/01_*.py
\`\`\`

## 연습문제
- `exercises/` 의 TODO를 채우고, `solutions/` 와 비교한다.
- (Phase 1에서 채워짐)
```

나머지 16개도 같은 패턴으로, 제목과 Phase 번호만 표대로 바꿔 작성한다.

- [ ] **Step 4: 17개 README가 모두 생성됐는지 확인**

Run:
```bash
ls -1 */README.md | grep -v -E '(docs|00_setup)' | wc -l
```
Expected: `17`

Run:
```bash
head -3 01_basics/README.md
head -3 17_capstone/README.md
```
Expected: 각각 올바른 제목과 Phase가 보인다.

---

## Task 6: `00_setup` 콘텐츠 작성

Phase 0에서 유일하게 실제 학습 콘텐츠가 채워지는 폴더다. 학습자가 즉시 첫 실행을 체험할 수 있도록.

**Files:**
- Create: `00_setup/README.md`
- Create: `00_setup/01_hello.py`
- Create: `00_setup/02_about_uv.py`

- [ ] **Step 1: `00_setup` 폴더 생성**

Run:
```bash
mkdir -p 00_setup
```

- [ ] **Step 2: `00_setup/README.md` 작성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/00_setup/README.md`

내용:
```markdown
# 00_setup — 환경 세팅

> 본격적인 학습 전에 한 번만 거치는 단원입니다.

## 배우는 것
- uv 명령으로 가상환경을 만들고 의존성을 동기화하는 방법
- 학습 스크립트를 `uv run python ...` 으로 실행하는 방법
- `if __name__ == "__main__":` 데모 블록의 의미

## 학습 순서
1. `01_hello.py` — 첫 실행 체험
2. `02_about_uv.py` — 자주 쓸 uv 명령어 정리

## 실행 방법
\`\`\`bash
# 저장소 루트에서 한 번만:
uv sync

# 학습 스크립트 실행:
uv run python 00_setup/01_hello.py
uv run python 00_setup/02_about_uv.py
\`\`\`

## 연습문제
- 이 단원은 환경 세팅이므로 연습문제가 없습니다.
- 두 스크립트가 모두 오류 없이 실행되면 다음 폴더(`01_basics/`)로 진행하세요.
```

- [ ] **Step 3: `00_setup/01_hello.py` 작성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/00_setup/01_hello.py`

내용:
```python
"""첫 실행 체험.

다른 언어 출신을 위한 메모:
- 파이썬은 컴파일 단계 없이 `python <파일>` 만으로 즉시 실행된다.
- 우리는 `python` 대신 `uv run python` 을 쓴다 — 가상환경을 자동으로 활성화해 준다.
- 모든 학습 스크립트는 파일 끝의 `if __name__ == "__main__":` 블록을 실행 진입점으로 한다.
"""

# ──── 1. 가장 단순한 문장 ────

# print 는 표준 출력으로 한 줄을 찍는 내장 함수다. (괄호 필수 — print "..."는 문법 오류)
print("안녕, 파이썬!")

# ──── 2. f-string 으로 값 끼워 넣기 ────

name = "Kee"                                  # 변수 = 값
# f"...{변수}..." 형태가 가장 흔히 쓰는 문자열 포맷 방식이다.
print(f"환영합니다, {name} 님.")

# ──── 3. 다른 언어와의 차이 한 가지 ────

# 들여쓰기가 곧 블록이다 — 중괄호도, 세미콜론도 없다.
for i in range(3):                            # range(3) → 0, 1, 2 세 번 반복
    print(f"  반복 {i}")                       # 들여쓰기 4칸이 곧 for 블록의 본문


# ──── 데모 실행 ────
# 이 파일이 직접 실행됐을 때만 아래가 동작한다.
# 다른 파일에서 import 했을 때는 실행되지 않는다 — 모듈 재사용을 위한 관례다.
if __name__ == "__main__":
    print("---")
    print("실행 성공! 다음 단계로 진행하세요: uv run python 00_setup/02_about_uv.py")
```

- [ ] **Step 4: `00_setup/02_about_uv.py` 작성**

파일 경로: `/Users/keesoonpark/Workspace/python-tutorial/00_setup/02_about_uv.py`

내용:
```python
"""자주 쓸 uv 명령어 정리.

uv 는 Rust 로 만든 파이썬 패키지 관리자다 (pip + venv + pyenv 역할을 한 도구로 통합).
이 파일은 실제로 uv 를 부르지 않고, 명령어를 문자열로 출력만 한다.
실행하면 "어떤 명령을 어떤 상황에서 쓰는가" 를 한눈에 볼 수 있다.
"""

import sys                              # 표준 라이브러리. 인터프리터 정보를 얻을 때 쓴다.


# ──── 1. 현재 파이썬 환경 확인 ────

# sys.executable 은 지금 실행 중인 파이썬 인터프리터의 경로다.
# `uv run python ...` 으로 돌렸다면 `.venv/bin/python` 비슷한 경로가 나온다.
print(f"인터프리터 경로: {sys.executable}")
print(f"파이썬 버전:     {sys.version.split()[0]}")


# ──── 2. 알아둘 uv 명령 ────

# 학습 중 가장 자주 쓰게 될 명령들 — 단순 문자열로 안내만 한다.
commands = [
    ("uv venv",                        "가상환경(.venv)을 만든다. uv sync 가 자동으로 호출하므로 보통 직접 칠 일은 없다."),
    ("uv sync",                        "pyproject.toml 의 dependencies 를 .venv 에 동기화한다."),
    ("uv pip install -e \".[data]\"",  "선택 그룹(data)을 추가 설치한다. Phase 4 진입 시 사용."),
    ("uv run python <파일>",            "가상환경을 자동 활성화해서 파이썬 스크립트를 실행한다."),
    ("uv add <패키지>",                  "새 의존성을 추가하고 pyproject.toml 에 기록한다."),
    ("uv remove <패키지>",               "의존성을 제거한다."),
    ("uv lock",                        "잠금 파일(uv.lock)을 갱신한다. 재현 가능한 환경을 위해."),
]

# 보기 좋게 표로 출력 — f-string 안의 `:<28` 는 28칸 너비 왼쪽 정렬을 뜻한다.
for cmd, desc in commands:
    print(f"  {cmd:<28} {desc}")


# ──── 데모 실행 ────
if __name__ == "__main__":
    print("---")
    print("이 단원은 끝났습니다. 다음 폴더: 01_basics/")
```

---

## Task 7: 전체 골격 스모크 테스트

Phase 0 결과물이 실제로 굴러가는지 한 번에 확인한다.

**Files:** 없음 (검증만)

- [ ] **Step 1: 루트 구조 점검**

Run:
```bash
ls -d */ | sort
```
Expected (정확히 이 순서로 19개 폴더가 보여야 한다 — `docs/`, `.omc/`는 별개):
```
00_setup/
01_basics/
02_data_structures/
03_functions/
04_modules_packages/
05_oop/
06_errors_exceptions/
07_io_files/
08_iterators_generators/
09_advanced_python/
10_typing/
11_concurrency/
12_testing/
13_data_science/
14_web_backend/
15_automation/
16_tooling_packaging/
17_capstone/
docs/
```

- [ ] **Step 2: 모든 README가 한국어로 작성됐는지 확인**

Run:
```bash
for d in 0*/  1*/; do
  echo "=== $d ==="
  head -1 "$d/README.md"
done
```
Expected: 18개 폴더 모두 `# NN_... — ...` 형태의 한국어 제목이 출력된다.

- [ ] **Step 3: `uv sync`가 깨끗하게 통과하는지 재확인**

Run:
```bash
uv sync
```
Expected: 에러 없음. "Audited 0 packages" 또는 비슷한 메시지.

- [ ] **Step 4: `00_setup/01_hello.py` 실행**

Run:
```bash
uv run python 00_setup/01_hello.py
```
Expected (정확한 출력):
```
안녕, 파이썬!
환영합니다, Kee 님.
  반복 0
  반복 1
  반복 2
---
실행 성공! 다음 단계로 진행하세요: uv run python 00_setup/02_about_uv.py
```

- [ ] **Step 5: `00_setup/02_about_uv.py` 실행**

Run:
```bash
uv run python 00_setup/02_about_uv.py
```
Expected:
- 인터프리터 경로에 `.venv/bin/python` 이 포함된다.
- 파이썬 버전이 `3.12.x` 로 출력된다.
- 7개 uv 명령이 정렬된 표 형식으로 출력된다.
- 마지막에 `이 단원은 끝났습니다. 다음 폴더: 01_basics/` 가 보인다.

- [ ] **Step 6: 사용자 검토 요청**

다음을 사용자에게 알린다:
> "Phase 0 골격 구축 완료. 18개 폴더가 만들어졌고, `00_setup`의 두 스크립트가 실제로 실행됩니다. 검토해보시고 다음 Phase 1 계획서 작성으로 넘어가도 될지 알려주세요."

검토 후 사용자가 OK 하면 Phase 1 (`01_basics` ~ `04_modules_packages`) 계획서를 별도 파일로 작성한다.

---

## Self-Review (계획 작성 후 점검)

**1. 스펙 커버리지:**
- [x] §3 전체 커리큘럼 폴더 구조 — Task 5에서 17개 폴더 + Task 6에서 00_setup
- [x] §4 README 4단 템플릿 — Task 5 Step 2 템플릿과 Task 6 Step 2 실제 적용
- [x] §6 환경/의존성 (pyproject.toml + uv) — Task 3
- [x] §2.4 파일 스타일(4원칙) — Task 6의 `01_hello.py`/`02_about_uv.py`가 표준 예시 역할
- [x] §7 Phase별 단계 제작 — 이 문서는 Phase 0만 다룬다, 명시됨

스펙의 §5(연습문제 형식)는 Phase 0 범위 밖이다 (`00_setup`은 연습문제가 없는 예외 단원). Phase 1 계획서에서 처음 적용된다.

**2. Placeholder 검사:** TBD/TODO/"나중에" 없음. (placeholder README의 "(Phase N에서 채워짐)" 은 의도된 placeholder임을 명시적으로 표기.)

**3. 타입 일관성:** 일관성 적용 대상 코드가 거의 없음 (설정 + README 위주). `pyproject.toml` 그룹명(`data`/`web`/`auto`/`test`/`typing`/`dev`)이 루트 README, Task 3, 스펙 §6.2에서 모두 일치하는 것 확인됨.

**4. 모호성:** `pyproject.toml` 의 hatch 빌드 단계에서 에러 발생 가능성에 대한 폴백 명시(Task 3 Step 2).

---

## 다음 Phase 안내

Phase 0이 완료되어 사용자 검토를 받은 뒤, **별도 계획서**로 Phase 1을 작성한다:
`docs/superpowers/plans/2026-05-22-python-tutorial-phase-1-basics.md` (작성 시점의 날짜 기준)

Phase 1 범위:
- `01_basics/`, `02_data_structures/`, `03_functions/`, `04_modules_packages/`
- 각 폴더에 학습 스크립트 5~8개, README 본문 채우기, `exercises/` + `solutions/` 추가
