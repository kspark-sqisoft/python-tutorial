# Python Tutorial — Phase 3 (고급) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development.

**Goal:** Phase 3 세 개 폴더(`09_advanced_python`, `10_typing`, `11_concurrency`)에 학습 스크립트·연습문제·정답을 채우고 README 갱신, 폴더 단위로 커밋.

**Architecture:** 폴더 단위 서브에이전트 패턴 (Phase 1~2와 동일). `10_typing` 진입 시 `uv pip install -e ".[typing]"` 로 mypy 설치 — 검증에 사용.

**Tech Stack:** Python 3.12, mypy(타이핑 검증용), 표준 라이브러리 threading/multiprocessing/asyncio.

**참조:** 스펙 `docs/superpowers/specs/2026-05-21-python-tutorial-design.md`
**선행:** Phase 0~2 완료.

---

## 스타일 규칙 (Phase 2 + 새 허용)

- 학습 스크립트: docstring 3~5줄 + `# ──── N. 소제목 ────` 구분선 + 한국어 주석 + `if __name__ == "__main__":` 데모 + 영어 snake_case 식별자.
- **새로 허용 (Phase 3):** 데코레이터, contextmanager, **타입 힌트** (10_typing 부터 본격), asyncio.
- **여전히 금지:** 외부 라이브러리 (mypy 는 검증 도구로만 사용, 학습 스크립트는 표준 라이브러리만).
- 연습문제 / 정답: 동일한 TODO + assert + `print("OK")` 패턴. 빈 exercise 는 실패해야.

---

## Task 1: `09_advanced_python/` — 데코레이터·컨텍스트 매니저·디스크립터

### 학습 스크립트 (4)

**`01_decorators.py`** — 함수 데코레이터
- 데코레이터 = 함수를 받아 함수를 반환하는 함수
- `@deco` 문법 설탕이 `f = deco(f)` 와 동일
- 가장 단순한 데코레이터: `def log(fn): def wrapper(*a, **kw): print("call"); return fn(*a, **kw); return wrapper`
- 인자 받는 데코레이터 (3중첩): `def repeat(n): def deco(fn): def wrapper(...): ...; return wrapper; return deco`
- `functools.wraps` 의 역할 (원본 함수의 `__name__`, docstring 보존)
- 클래스 메서드 데코: `@staticmethod`, `@classmethod` (한 줄 언급, 자세히는 OOP에서 다룸)
- Demo: `@log` 적용한 add 함수, `@repeat(3)` 적용한 print

**`02_context_managers.py`** — 컨텍스트 매니저
- with 가 동작하는 원리: `__enter__` / `__exit__`
- 클래스 기반: `class Timer: def __enter__(self): ...; def __exit__(self, exc_type, exc, tb): ...`
- 함수 기반: `from contextlib import contextmanager` + `@contextmanager` + `yield`
- 예외 발생 시에도 `__exit__` 실행 — 자원 정리에 강력
- Demo: Timer 클래스 + @contextmanager 두 가지 모두

**`03_descriptors.py`** — 디스크립터 (간단히)
- 디스크립터 = `__get__`, `__set__`, `__delete__` 메서드를 가진 클래스
- @property 가 디스크립터로 구현되어 있음을 한 줄 언급
- 데이터 검증용 디스크립터 예제: `Positive` (음수 대입 시 ValueError)
- Demo: `class Order: amount = Positive()` 형태로 검증 동작

**`04_metaclasses_intro.py`** — 메타클래스 맛보기
- type(obj) → 클래스, type(클래스) → 메타클래스
- 모든 클래스의 기본 메타클래스는 `type`
- 메타클래스로 클래스 생성을 제어할 수 있다 — 라이브러리 저자들이 가끔 사용
- 보통 학습자는 직접 만들 일이 없음 — 이런 게 있다는 것만
- Demo: `type("Foo", (), {"x": 1})` 로 클래스 동적 생성 1줄, 메타클래스 한 예제(`__init_subclass__` 로 대체 권장 한 줄 언급)

### Exercises (4)

- `ex01_decorators`: `timing` 데코레이터 작성 — 함수 실행 시간을 dict 에 기록. assert 로 호출 후 기록 존재 확인.
- `ex02_context_managers`: `Suppress(ValueError)` 컨텍스트 매니저 — with 안에서 ValueError 발생하면 무시, 다른 예외는 그대로. assert.
- `ex03_descriptors`: `NonNegative` 디스크립터 — 음수 대입 시 ValueError, 양수/0 은 정상. 클래스에 적용 후 동작 확인.
- `ex04_metaclasses_intro`: `type("Dynamic", (), {"greet": lambda self: "hi"})` 로 클래스 동적 생성 후 인스턴스화·메서드 호출. assert.

### Solutions (4)

### README

```
# 09_advanced_python — 데코레이터·컨텍스트·디스크립터

## 배우는 것
- 함수 데코레이터 (단일/인자 받는/functools.wraps)
- 컨텍스트 매니저 (클래스 기반 + @contextmanager)
- 디스크립터 — @property 의 정체
- 메타클래스 맛보기 (type 동적 생성)

## 학습 순서
1. `01_decorators.py`
2. `02_context_managers.py`
3. `03_descriptors.py`
4. `04_metaclasses_intro.py`

## 실행 방법
[bash] uv run python 09_advanced_python/01_decorators.py [/bash]

## 연습문제
- exercises/ex01_*.py ~ ex04_*.py TODO 채우기.
```

### Steps: 표준 9단계.

커밋:
```
git commit -m "feat(09_advanced_python): 데코레이터/컨텍스트/디스크립터/메타클래스 — 학습 4 + 연습 4 + 정답 4"
```

---

## Task 2: `10_typing/` — 타입 힌트

### 사전 준비
실행자가 먼저 `uv pip install -e ".[typing]"` 으로 mypy 를 설치한다. 그 다음 학습 스크립트 작성.

### 학습 스크립트 (5)

**`01_basic_hints.py`** — 기본 타입 힌트
- 변수 힌트: `name: str = "Kee"`, `age: int = 30`
- 함수 시그니처: `def add(a: int, b: int) -> int:`
- 컨테이너: `list[int]`, `dict[str, int]`, `tuple[int, str, bool]`, `set[str]` (Python 3.9+)
- `Optional[X]` = `X | None` (Python 3.10+ union 문법 선호)
- 타입 힌트는 **런타임에 강제되지 않는다** — mypy 같은 정적 검사기가 검증
- Demo: 힌트 있는 함수 호출 + 잘못된 타입 호출 시 mypy 가 잡지만 런타임은 통과 (주석으로 명시)

**`02_typed_dict_protocol.py`** — TypedDict 와 Protocol
- `from typing import TypedDict`
  - `class UserDict(TypedDict): name: str; age: int`
  - dict 의 키·값 타입 명시 (실제론 평범한 dict)
- `from typing import Protocol`
  - `class HasArea(Protocol): def area(self) -> float: ...`
  - 구조적 부분 타입 (덕 타이핑의 정적 버전)
- Demo: TypedDict 인스턴스, Protocol 만족하는 클래스

**`03_generics.py`** — 제네릭
- `from typing import TypeVar, Generic` (예전 문법)
- Python 3.12 의 새 PEP 695 문법: `def first[T](items: list[T]) -> T:`
- `class Stack[T]: ...` (3.12 새 문법)
- Demo: 제네릭 함수 first, 제네릭 클래스 Stack

**`04_mypy_check.py`** — mypy 로 검증
- `# type: ignore` 주석 한 줄 언급
- 의도적으로 타입 에러를 일으키는 함수, 정상인 함수 두 개 정의
- 데모 출력: mypy 명령으로 검사하는 방법을 print 로 안내 (`mypy 10_typing/04_mypy_check.py` 같이)
- 실제 mypy 실행은 학습자가 수동으로
- Demo: print 로 mypy 사용법 안내

**`05_real_world_patterns.py`** — 자주 보는 실전 패턴
- `Callable[[int, int], int]` — 함수 타입
- `Literal["GET", "POST"]` — 문자열 enum 식
- `Final` — 재할당 금지
- `cast` — 타입 단언
- Demo: 한 가지씩 짧은 사용 예

### Exercises (5)

- `ex01_basic_hints`: 함수 `def repeat(s: str, n: int) -> str:` 작성 (반복 문자열). assert + 힌트 검증.
- `ex02_typed_dict_protocol`: `TypedDict` 로 `Book(title, pages)` 정의 + 생성. Protocol `HasLength(__len__)` 만족하는 list 확인.
- `ex03_generics`: PEP 695 문법으로 `def last[T](items: list[T]) -> T | None:` 작성 (마지막 원소 또는 None).
- `ex04_mypy_check`: 학습자가 mypy 명령을 직접 실행해 보는 안내 — 정답 파일에는 mypy 가 통과하는 코드, exercise 파일에는 mypy 가 실패하는 코드 (의도된 에러). assert 는 단순히 함수 동작만 검증.
- `ex05_real_world_patterns`: `Callable[[int], int]` 받는 `apply(fn, x)` 작성. assert.

### Solutions (5)

### README

```
# 10_typing — 타입 힌트

## 사전 준비
[bash] uv pip install -e ".[typing]" [/bash]

## 배우는 것
- 기본 타입 힌트 (변수/함수/컨테이너/Optional)
- TypedDict, Protocol (구조적 부분 타입)
- 제네릭 (PEP 695 새 문법: `def f[T](...)`)
- mypy 로 정적 검증
- 실전 패턴 (Callable/Literal/Final/cast)

## 학습 순서
1. `01_basic_hints.py`
2. `02_typed_dict_protocol.py`
3. `03_generics.py`
4. `04_mypy_check.py`
5. `05_real_world_patterns.py`

## 실행 방법
[bash] uv run python 10_typing/01_basic_hints.py [/bash]

## mypy 로 정적 검증
[bash] uv run mypy 10_typing/ [/bash]

## 연습문제
- exercises/ex01_*.py ~ ex05_*.py TODO 채우기.
```

### Steps

1. `uv pip install -e ".[typing]"` 으로 mypy 설치
2. `mkdir -p 10_typing/exercises 10_typing/solutions`
3-5. 학습 5 / exercises 5 / solutions 5
6. README 교체
7-9. 검증 (런타임만, mypy 는 학습자가 수동 실행)
10. `uv run mypy 10_typing/solutions/` 가 통과해야 함 (정답들은 타입 깨끗) 확인
11. 커밋:
```
git add 10_typing/ pyproject.toml uv.lock
git commit -m "feat(10_typing): 타입 힌트 / TypedDict / Protocol / 제네릭(PEP 695) / mypy — 학습 5 + 연습 5 + 정답 5"
```

---

## Task 3: `11_concurrency/` — 동시성

### 학습 스크립트 (5)

**`01_threading.py`** — threading
- `from threading import Thread`
- `Thread(target=fn, args=(...)).start()`, `.join()`
- GIL 때문에 CPU-bound 에는 효과 없음, IO-bound 에 유리 (한 줄 강조)
- `Lock`, `RLock` 으로 공유 자원 보호
- Demo: 두 스레드로 1초씩 잠자기(IO 시뮬레이션) → 직렬보다 빠름

**`02_concurrent_futures.py`** — concurrent.futures
- `ThreadPoolExecutor`, `ProcessPoolExecutor`
- `executor.submit(fn, ...)` → Future 객체
- `executor.map(fn, iter)` 로 일괄 처리
- `with executor:` 패턴으로 자동 종료
- Demo: ThreadPoolExecutor 로 IO 시뮬레이션 5개 병렬 처리

**`03_multiprocessing.py`** — multiprocessing
- `from multiprocessing import Process, Pool`
- 새 프로세스 = 별도 메모리 공간 (GIL 회피, CPU-bound 에 효과)
- macOS·Windows 에선 'spawn' 시작 방식 — `if __name__ == "__main__":` 가드 필수
- 데이터 공유 어려움 — Queue/Pipe/Manager 한 줄 언급
- Demo: Pool(2) 로 CPU 작업 2개 병렬 — 단순 계산(예: 1~N 합) 두 번. **`if __name__ == "__main__":` 가드 안에서만 실행**.

**`04_asyncio_basics.py`** — asyncio 기본
- `async def` / `await` 문법
- `asyncio.run(main())` 으로 이벤트 루프 시작
- `asyncio.sleep(t)` 은 비차단 (스레드 sleep 과 다름)
- `asyncio.gather(...)` 로 여러 코루틴 동시 실행
- Demo: 3개 코루틴이 각각 1초씩 sleep → 총 1초 (직렬은 3초)

**`05_async_io_bound.py`** — asyncio 활용
- IO-bound 작업의 진짜 효과: 가짜 "네트워크 호출" 함수(asyncio.sleep 으로 시뮬레이션) 10개 동시 실행
- async for / async with (한 줄 소개)
- 동기 코드와의 차이점 정리표 형태 출력
- Demo: 10개 가짜 IO 작업 직렬(약 5초) vs gather(약 0.5초) 비교 출력

### Exercises (5)

- `ex01_threading`: 2개 스레드로 각 0.3초 sleep 동시 실행 → 총 시간이 0.5초 미만임을 assert (`time.time()` 으로 측정).
- `ex02_concurrent_futures`: ThreadPoolExecutor 로 `[sleep_then(i) for i in 1..5]` 동시 실행 (각 0.2초). 총 시간 < 0.5초 assert. 결과 합계 검증.
- `ex03_multiprocessing`: Pool(2) 로 [1, 2, 3, 4] 의 제곱 병렬 계산 (`if __name__ == "__main__":` 안에서). 결과 `[1, 4, 9, 16]` assert.
- `ex04_asyncio_basics`: 두 코루틴이 각각 0.3초 sleep, gather 로 동시 실행. 총 시간 < 0.5초 assert.
- `ex05_async_io_bound`: 5개 가짜 IO 작업(각 0.2초) 동시 실행, 총 합산 결과 검증 + 시간 < 0.5초 assert.

각 exercise 는 짧고 시간 측정에 너무 빡빡하지 않게 — CI 환경의 지터 고려해 여유 있게.

### Solutions (5)

### README

```
# 11_concurrency — 동시성

## 배우는 것
- threading + GIL 의미 (IO-bound 에 유리)
- concurrent.futures 의 ThreadPoolExecutor / ProcessPoolExecutor
- multiprocessing (CPU-bound, 별도 메모리, spawn 가드)
- asyncio (async/await, asyncio.run, gather)
- 동기/비동기 IO 비교

## 학습 순서
1. `01_threading.py`
2. `02_concurrent_futures.py`
3. `03_multiprocessing.py`
4. `04_asyncio_basics.py`
5. `05_async_io_bound.py`

## 실행 방법
[bash] uv run python 11_concurrency/01_threading.py [/bash]

## 주의
- 멀티프로세싱 예제는 `if __name__ == "__main__":` 안에서만 실행됩니다 (macOS/Windows 의 spawn 방식 요구).

## 연습문제
- exercises/ex01_*.py ~ ex05_*.py TODO 채우기.
```

### Steps: 표준 9단계.

커밋:
```
git commit -m "feat(11_concurrency): threading / concurrent.futures / multiprocessing / asyncio — 학습 5 + 연습 5 + 정답 5"
```

---

## Phase 3 종합 검증 (마지막 Task 후)

```bash
for d in 09_advanced_python 10_typing 11_concurrency; do
  for f in $d/0[1-9]_*.py; do
    uv run python "$f" >/dev/null && echo "OK $f" || echo "FAIL $f"
  done
  for f in $d/solutions/ex*.py; do
    out=$(uv run python "$f")
    [ "$out" = "OK" ] && echo "PASS $f" || echo "FAIL $f -> $out"
  done
done
uv run mypy 10_typing/solutions/ && echo "mypy on solutions: clean" || echo "mypy on solutions: had issues"
```

---

## 다음 Phase 안내

Phase 3 완료 후 Phase 4 (`12_testing`, `13_data_science`, `14_web_backend`, `15_automation`, `16_tooling_packaging`) 계획서 작성. 각 폴더에서 해당 optional-dependencies 그룹을 설치한다.
