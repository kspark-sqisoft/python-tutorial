# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 성격

다른 언어 경험자를 위한 **파이썬 학습 저장소**다. 프로덕션 코드가 아니라 교재이므로,
파이썬 idiom(EAFP, 컴프리헨션, 언패킹, duck typing 등) 위주로 한 줄씩 주석을 달아 설명한다.

- Python 3.12 고정(`.python-version`), 패키지 관리는 `uv`
- Phase 1~3은 표준 라이브러리만 사용 → 추가 설치 불필요
- Phase 4 이후는 `pyproject.toml`의 `optional-dependencies` 그룹을 진입 시점에 설치

## 명령어

### 환경
```bash
uv sync                          # 최초 1회 — 3.12 설치 + .venv 생성
uv pip install -e ".[test]"      # 12_testing 진입 시
uv pip install -e ".[typing]"    # 10_typing
uv pip install -e ".[data]"      # 13_data_science
uv pip install -e ".[web]"       # 14_web_backend
uv pip install -e ".[auto]"      # 15_automation
uv pip install -e ".[dev]"       # 16_tooling_packaging (ruff, black)
```

### 학습 스크립트 실행
모든 `.py`는 단독 실행 가능. 항상 저장소 루트에서 절대 경로로 호출:
```bash
uv run python 02_data_structures/01_list.py
```

### 테스트
```bash
uv run pytest 17_capstone/ -q                       # capstone 전체 (todo_cli 9 + book_api 5)
uv run pytest 17_capstone/01_todo_cli/tests/ -q     # 단일 프로젝트
uv run pytest 12_testing/exercises/ -q              # 학습용 pytest 연습
uv run pytest 17_capstone/01_todo_cli/tests/test_storage.py::test_load_empty -q   # 단일 테스트
```

### Capstone 실행
폴더 이름이 숫자로 시작해 `python -m` 형식 import가 안 된다. 파일 경로 직접 지정 또는 폴더 진입 후 실행:
```bash
uv run python 17_capstone/01_todo_cli/src/cli.py add "장보기" --db /tmp/_todos.json
uv run python 17_capstone/02_book_api/src/app.py
cd 17_capstone/02_book_api && uv run uvicorn src.app:app --reload   # http://127.0.0.1:8000/docs
```

## 코드 작성 규칙 (학습 자료 톤)

설계 문서: `docs/superpowers/specs/2026-05-21-python-tutorial-design.md` — 톤·형식의 단일 출처.

### 주석 4원칙 (모든 학습 `.py` 적용)
1. **모듈 docstring** 상단에 — 다루는 개념 + 다른 언어와의 차이를 3~5줄.
2. **블록 구분선** — `# ──── 1. 제목 ────` (한국어 박스 드로잉 문자).
3. **개념 첫 등장 시 줄 단위 주석**. 반복은 생략해 노이즈 줄이기.
4. **파일 끝에 `if __name__ == "__main__":`** 데모 블록 — 의미 있는 출력이 나와야 함.

### 언어
- 주석·README·docstring: **한국어**
- 코드 식별자(변수/함수/클래스): **영어** (실무 통용 형태)

### 폴더 단위(Unit) 구성
각 학습 폴더는 다음 3종 산출물 + README:
- `NN_topic.py` — 한 파일은 한 개 핵심 개념만
- `exercises/exNN_topic.py` — TODO + `assert` 자가 채점, 성공 시 `print("OK")`
- `solutions/exNN_topic.py` — 같은 파일을 채운 정답 + 상단에 "왜 이렇게 풀었나" docstring 한 문단
- `README.md` — 4단 구성(배우는 것 / 학습 순서 / 실행 방법 / 연습문제)

`12_testing/`만 예외 — 연습문제도 pytest `test_*.py` 형식을 따른다(학습 주제가 pytest 자체이므로).

## 아키텍처 메모

### Phase 진행 (이미 완료)
Phase 0~5 모두 완성된 상태. 새 폴더를 추가하기보다 기존 폴더의 스크립트/연습문제를 보강·수정하는 작업이 대부분이다. Phase별 계획서는 `docs/superpowers/plans/2026-05-2*-python-tutorial-phase-*.md` 참고.

### 토픽 매핑 메모
모두 같은 파일 끝에 **Dart/TypeScript 비교 섹션**을 포함한다. 다른 폴더에 동일 내용을 중복 작성하지 말 것.

- 값/참조 타입 + 함수 인자 전달 모델 + `is`/`==` + 가변 기본 인자 함정 → `02_data_structures/07_value_vs_reference.py`
- 얕은/깊은 복사·불변성 유지 패턴(`copy` 모듈, `MappingProxyType`, frozen dataclass) → `02_data_structures/08_copy_immutability.py`
- `enum` (Enum/IntEnum/StrEnum, auto, 멤버에 부가 정보, match 와 결합) → `05_oop/06_enum.py`
- `abc.ABC` vs `Protocol` 비교 (명시적 상속 강제 vs 구조적 타이핑, `runtime_checkable`) → `05_oop/07_abc.py`
- `__slots__` 와 `@dataclass(slots=True)`, 자식 클래스에서 슬롯 유지 함정 → `05_oop/08_slots.py`
- 예외 chaining: `raise X from Y`, `__cause__`/`__context__`, `from None`, `ExceptionGroup` + `except*` → `06_errors_exceptions/06_chaining.py`
- 구조적 패턴 매칭 본격편(리터럴/시퀀스/매핑/클래스 패턴 + 가드 + 캡처 함정) → `09_advanced_python/05_pattern_matching.py`

### Windows 콘솔 호환성 메모
이 저장소의 학습 데모는 `cp949` 콘솔에서 `uv run python` 으로 실행될 수 있다. `print()` 인자에 cp949로 인코딩 불가한 비ASCII 기호(예: em dash `—`, 근사기호 `≈`)는 `UnicodeEncodeError`를 일으킨다. 주석에는 자유롭게 쓰되, **`print` 인자에는 ASCII 또는 한글만 사용**한다(`-`, `~`, `->`, `<-` 등으로 대체).

### `17_capstone/` 구조 주의점
- 폴더명이 숫자로 시작해 패키지 import가 불가능. 두 프로젝트 모두 `src/` 안에 모듈을 두고 직접 파일 경로로 실행한다.
- **`17_capstone/tests/__init__.py`가 없는 것이 의도된 상태**다 — 두 하위 프로젝트 모두 `tests/` 디렉터리를 가지므로, 상위에 `__init__.py`를 두면 pytest 수집 시 `tests` 패키지 이름이 충돌한다(커밋 51fb0c2 참고).
- `02_book_api`는 SQLAlchemy 2.x `Mapped` 스타일 + in-memory SQLite + FastAPI `lifespan`으로 DB 초기화. 테스트는 `conftest.py`에서 DB 리셋 후 `TestClient` 픽스처 주입.

### 의존성 그룹 매핑
`pyproject.toml`의 `optional-dependencies`:
| 그룹 | 폴더 | 패키지 |
|------|------|--------|
| `test` | 12_testing, 17_capstone | pytest, pytest-cov |
| `typing` | 10_typing | mypy |
| `data` | 13_data_science | numpy, pandas, matplotlib, jupyter |
| `web` | 14_web_backend, 17_capstone/02_book_api | fastapi, uvicorn, requests, pydantic, sqlalchemy |
| `auto` | 15_automation | beautifulsoup4, click |
| `dev` | 16_tooling_packaging | ruff, black |

빌드 대상이 없는 학습 저장소이므로 `[tool.hatch.build.targets.wheel]`에 `bypass-selection = true`로 설정되어 있다.
