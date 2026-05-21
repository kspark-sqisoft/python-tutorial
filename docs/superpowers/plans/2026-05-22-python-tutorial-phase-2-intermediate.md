# Python Tutorial — Phase 2 (중급) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development.

**Goal:** Phase 2 네 개 폴더(`05_oop`, `06_errors_exceptions`, `07_io_files`, `08_iterators_generators`)에 학습 스크립트·연습문제·정답을 채우고 README를 갱신, 폴더 단위로 커밋.

**Architecture:** Phase 1과 동일한 폴더-단위 서브에이전트 패턴. 한 서브에이전트가 한 폴더 안의 모든 산출물(학습·exercise·solution·README)을 작성하고, 본인이 검증·커밋까지 마친다.

**Tech Stack:** Python 3.12, 표준 라이브러리만 사용 (json, csv, pathlib, itertools 등).

**참조:**
- 스펙 `docs/superpowers/specs/2026-05-21-python-tutorial-design.md`
- Phase 0 (`24b04ab`), Phase 1 (`2444b10`, `1dcada5`, `a671648`, `8e99cb1`, `e74fb36`) 완료.

---

## 모든 파일에 강제되는 스타일 규칙 (Phase 1과 동일)

학습 스크립트:
1. 모듈 docstring 3~5줄 (개념 + 다른 언어 차이).
2. 섹션 구분선 `# ──── N. 소제목 ────` (U+2500 박스 라인 문자, 양쪽 4개씩).
3. 개념 첫 등장 시 한국어 줄 단위 주석.
4. 파일 끝 `if __name__ == "__main__":` 데모 블록.
5. 식별자 영어 snake_case (클래스는 PascalCase), 주석·문자열 한국어.
6. **Phase 2에서 새로 허용**: `class`, `try/except`, JSON/CSV 표준 라이브러리.
7. 여전히 금지: 외부 라이브러리, 타입 힌트 (10_typing 에서 본격 도입).

연습문제·정답: Phase 1과 같은 규칙 (TODO + assert + `print("OK")`, 빈 상태 실패, 정답은 OK만 출력).

---

## Task 1: `05_oop/` — 객체지향 프로그래밍

**Files:**
- Modify: `05_oop/README.md`
- Create: 5 학습 스크립트, 5 exercises, 5 solutions

### 학습 스크립트 (5)

**`01_classes.py`** — 클래스 기본
- `class Point:` 선언, `__init__(self, x, y)`
- 인스턴스 속성 vs 클래스 속성
- 메서드 정의 (`def distance_to(self, other):`)
- `__init__` 의 의미 (생성자가 아닌 초기화자)
- self 의 의미 (자바 this 와 비슷하지만 명시적 첫 인자)
- `class Counter:` 에 클래스 속성 `total` 두고 인스턴스마다 증가하는 예제로 클래스/인스턴스 속성 구분
- Demo: Point(3,4) 와 Point(0,0) 만들어 distance_to 호출

**`02_inheritance.py`** — 상속과 다형성
- `class Dog(Animal):` 형태 선언
- `super().__init__(...)` 부모 초기화
- 메서드 오버라이드
- `isinstance(d, Animal)`, `issubclass(Dog, Animal)`
- 다중 상속 한 줄 언급 (MRO는 깊이 안 다룸)
- 다형성: 같은 메서드 이름으로 다른 동작
- Demo: Animal 베이스 + Dog/Cat 자식, sound() 다형성

**`03_magic_methods.py`** — 매직 메서드 (던더 메서드)
- `__init__`, `__repr__`, `__str__` 차이
- `__eq__`, `__hash__` (둘 다 같이 정의해야 함을 한 줄 강조)
- `__len__`, `__iter__`, `__contains__`
- `__add__` 같은 연산자 오버로딩
- Demo: `Vector(2, 3) + Vector(1, 4)`, `len(MyBag(...))`, `for x in MyBag(...)`

**`04_dataclass.py`** — dataclass
- `from dataclasses import dataclass, field`
- `@dataclass` 가 자동 만들어주는 `__init__`, `__repr__`, `__eq__`
- `frozen=True` 로 불변
- `field(default_factory=list)` — 가변 기본값 함정 회피
- 일반 클래스로 같은 걸 만들면 얼마나 boilerplate 가 줄어드는지 한 줄 비교
- Demo: `@dataclass class User: name; age=0` 만들고 비교·출력·복사 시연

**`05_property.py`** — property 와 캡슐화
- `@property` 로 getter
- `@<name>.setter` 로 setter (검증 로직 넣기)
- `_attr` 관례 (private 약속), `__attr` (네임 맹글링 한 줄 언급)
- 자바의 getter/setter 대비 더 간결함
- Demo: `Temperature` 클래스에 celsius 프로퍼티(setter 에서 절대영도 이하 거부), fahrenheit getter 추가

### Exercises (5)

- `ex01_classes.py`: `Rectangle(width, height)` 클래스 — `area()`, `perimeter()` 메서드. assert 로 검증.
- `ex02_inheritance.py`: `Animal` 베이스 + `Dog(Animal)` 자식 — `Dog.sound() == "멍"`, `Animal.sound() == "..."` 형태로 폴리모피즘 assert.
- `ex03_magic_methods.py`: `Vector` 클래스에 `__add__`, `__eq__` 구현. `Vector(1,2) + Vector(3,4) == Vector(4,6)` assert.
- `ex04_dataclass.py`: `@dataclass(frozen=True) class Point` 두 개 만들어 `==` 비교, hash 가능 확인.
- `ex05_property.py`: `Account` 클래스에 `balance` 프로퍼티 + setter 에서 음수 거부 (`ValueError` 발생). assert + try/except 로 검증.

### Solution 규칙: 같은 파일명, 풀이 의도 docstring, 실행 시 `OK`만.

### README 교체

```
# 05_oop — 객체지향 프로그래밍

## 배우는 것
- 클래스/인스턴스/메서드/self
- 상속, super(), 메서드 오버라이드, 다형성
- 매직 메서드 (__init__, __repr__, __eq__, __add__, ...)
- @dataclass — boilerplate 제거
- @property — 캡슐화 (자바 getter/setter 패턴과 비교)

## 학습 순서
1. `01_classes.py`
2. `02_inheritance.py`
3. `03_magic_methods.py`
4. `04_dataclass.py`
5. `05_property.py`

## 실행 방법
[bash] uv run python 05_oop/01_classes.py [/bash]

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 와 비교.
```

### Steps

1. `mkdir -p 05_oop/exercises 05_oop/solutions`
2. 학습 5 작성
3. exercises 5 작성
4. solutions 5 작성
5. README 교체
6. 학습 무오류 검증 / 정답 PASS 검증 / 빈 exercise 실패 검증
7. 커밋:
```
git add 05_oop/
git commit -m "feat(05_oop): 클래스/상속/매직메서드/dataclass/property — 학습 5 + 연습 5 + 정답 5"
```

---

## Task 2: `06_errors_exceptions/` — 예외 처리

### 학습 스크립트 (5)

**`01_try_except.py`** — try/except 기본
- `try: ... except 예외종류: ...` 기본 형태
- 여러 예외 한 번에 `except (ZeroDivisionError, ValueError):`
- `except 예외 as e:` 로 예외 객체 받기
- 빈 `except:` 가 왜 위험한지 (KeyboardInterrupt 도 잡힘)
- Demo: 0 나누기, int 변환 실패 잡기

**`02_else_finally.py`** — else, finally
- `try / except / else / finally` 4단 구조
- else: try 성공 시에만
- finally: 예외 발생/성공 무관 항상 실행
- 파일 정리, DB 연결 정리 같은 자원 정리 시 사용 (`with` 문이 보통 더 좋음을 한 줄 언급)
- Demo: 4단 구조 동작 보이기

**`03_raise_custom.py`** — raise 와 사용자 정의 예외
- `raise ValueError("메시지")`
- 사용자 정의: `class NegativeBalanceError(Exception):` 같은 형태
- 예외 계층 살짝 (Exception 상속받으면 보통은 충분)
- `raise NewErr() from original_err` (chained exception) 한 줄
- Demo: Account 에 입금/출금, 잔액 음수 시 사용자 예외

**`04_exception_hierarchy.py`** — 예외 계층
- 기본: BaseException → Exception → ValueError/TypeError/...
- 흔히 보는 것: KeyError, IndexError, FileNotFoundError, AttributeError, ZeroDivisionError, TypeError, ValueError
- 자식 예외는 부모로 잡힘 (`except Exception:` 이 거의 모두 잡음)
- 보통 `except Exception:` 까지만, `BaseException` 은 잡지 말 것 (SystemExit, KeyboardInterrupt 포함)
- Demo: 각 흔한 예외를 의도적으로 발생시켜 잡기

**`05_eafp.py`** — EAFP 와 LBYL
- EAFP (Easier to Ask Forgiveness than Permission) — 파이썬 관례
- LBYL (Look Before You Leap) — 다른 언어 관례
- dict 접근: `d.get(k)` (LBYL) vs `try d[k] except KeyError` (EAFP) — 어느 쪽이 더 파이썬다운지 상황별로
- 파일 열기: `if path.exists(): open(...)` vs `try open(...) except FileNotFoundError`
- 단순한 경우는 둘 다 OK, 동시성/경쟁 상황에선 EAFP 가 안전
- Demo: dict 접근 두 방식 비교, 파일 열기 두 방식 비교

### Exercises (5)

- `ex01_try_except`: 주어진 문자열 리스트 `["1", "2", "abc", "3"]` 에서 int 변환 가능한 것만 골라 `nums = [1, 2, 3]` 만들기 (try/except ValueError).
- `ex02_else_finally`: 주어진 함수에서 `executed_finally` 가 True 가 되는지 확인 (finally 절 실행 확인).
- `ex03_raise_custom`: `NegativeError` 사용자 예외 정의 + `must_be_positive(n)` 함수 작성 (음수면 raise). try/except 로 검증.
- `ex04_exception_hierarchy`: 5가지 표현식이 각각 어떤 예외를 발생시키는지 dict `errors` 에 매핑 (`{"div_zero": "ZeroDivisionError", ...}` 형태). assert.
- `ex05_eafp`: dict 에서 값 가져오는 함수를 EAFP 패턴으로 작성. assert.

### README

```
# 06_errors_exceptions — 예외 처리

## 배우는 것
- try / except / else / finally
- raise 와 사용자 정의 예외
- 흔한 예외 계층
- EAFP vs LBYL — 파이썬 관용

## 학습 순서
1. `01_try_except.py`
2. `02_else_finally.py`
3. `03_raise_custom.py`
4. `04_exception_hierarchy.py`
5. `05_eafp.py`

## 실행 방법
[bash] uv run python 06_errors_exceptions/01_try_except.py [/bash]

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
```

### Steps: Task 1과 같은 7단계.

커밋:
```
git commit -m "feat(06_errors_exceptions): try/except/else/finally/raise/EAFP — 학습 5 + 연습 5 + 정답 5"
```

---

## Task 3: `07_io_files/` — 파일 입출력

### 학습 스크립트 (6)

**`01_open_read_write.py`** — open(), read, write
- `open(path, "r"|"w"|"a"|"rb"|"wb")` 모드
- `read()`, `readline()`, `readlines()`, `for line in f:` (가장 권장)
- `write()`, `writelines()`
- 항상 `close()` 호출 — 또는 `with` 문 (다음 파일)
- `encoding="utf-8"` 명시 (한글 환경에서 자주 빠뜨림)
- Demo: 임시 파일에 쓰고 다시 읽기 (pathlib 사용)

**`02_with_statement.py`** — with (컨텍스트 매니저)
- `with open(...) as f:` 가 왜 더 안전한가 (예외 발생해도 자동 close)
- 여러 파일 동시: `with open(a) as fa, open(b) as fb:`
- 컨텍스트 매니저는 09_advanced_python 에서 직접 만들기 다룸을 한 줄 안내
- Demo: 두 파일 동시 처리

**`03_json.py`** — JSON 직렬화
- `import json`
- `json.dumps(obj)` 객체 → 문자열, `json.loads(s)` 문자열 → 객체
- `json.dump(obj, f)` 파일 쓰기, `json.load(f)` 파일 읽기
- `indent=2`, `ensure_ascii=False` (한글 그대로)
- dict/list/str/int/float/bool/None 만 변환 가능 (custom 객체는 default= 인자 한 줄)
- Demo: dict → 임시 .json 파일 → 다시 dict

**`04_csv.py`** — CSV 읽기/쓰기
- `import csv`
- `csv.reader(f)`, `csv.writer(f)` — 리스트 단위
- `csv.DictReader(f)`, `csv.DictWriter(f, fieldnames=...)` — dict 단위
- `newline=""` 항상 지정 (윈도우 호환)
- Demo: 임시 CSV 파일에 헤더 + 3행 쓰고 DictReader 로 읽기

**`05_pathlib_io.py`** — pathlib 으로 파일 입출력
- `Path("file.txt").read_text(encoding="utf-8")`, `.write_text(...)`
- `.read_bytes()`, `.write_bytes()`
- 가장 짧은 한 줄 파일 IO
- Demo: write_text + read_text 비교 (한글 포함)

**`06_temp_files.py`** — 임시 파일/디렉터리
- `tempfile` 모듈: `NamedTemporaryFile`, `TemporaryDirectory`
- 자동 정리되는 자원 — 학습 스크립트에서 안전하게 IO 시연용
- Demo: TemporaryDirectory 안에 파일 만들고 읽기

### Exercises (6)

- `ex01_open_read_write`: 임시 파일에 "안녕\n반가워" 두 줄 쓰고 다시 읽어서 줄 수 == 2 assert. tempfile 사용.
- `ex02_with_statement`: with 두 파일 동시 처리 — A 파일 읽어서 대문자로 B 파일에 쓰기. 검증.
- `ex03_json`: dict `{"name": "Kee", "scores": [90, 85]}` 를 JSON 직렬화/역직렬화 후 동일한지 assert. ensure_ascii=False 검증.
- `ex04_csv`: 3행 DictWriter 로 쓰고 DictReader 로 읽어 행 수·필드값 검증.
- `ex05_pathlib_io`: Path.write_text + read_text 왕복 — 한글 포함. encoding 명시 검증.
- `ex06_temp_files`: TemporaryDirectory 안에 파일 만들고 컨텍스트 종료 후 디렉터리가 사라지는지 assert (`Path.exists()` 가 False).

### README

```
# 07_io_files — 파일 입출력

## 배우는 것
- open(), read/write, encoding="utf-8"
- with 문으로 안전한 자원 정리
- JSON 직렬화/역직렬화 (한글 처리)
- CSV reader/writer + DictReader/DictWriter
- pathlib 의 read_text / write_text
- tempfile 로 안전한 임시 자원

## 학습 순서
1. `01_open_read_write.py`
2. `02_with_statement.py`
3. `03_json.py`
4. `04_csv.py`
5. `05_pathlib_io.py`
6. `06_temp_files.py`

## 실행 방법
[bash] uv run python 07_io_files/01_open_read_write.py [/bash]

## 연습문제
- `exercises/ex01_*.py` ~ `ex06_*.py` TODO 채우기.
```

### Steps: 같은 7단계.

커밋:
```
git commit -m "feat(07_io_files): open/with/json/csv/pathlib/tempfile — 학습 6 + 연습 6 + 정답 6"
```

---

## Task 4: `08_iterators_generators/` — 이터레이터와 제너레이터

### 학습 스크립트 (5)

**`01_iter_next.py`** — 이터레이터 프로토콜
- `iter(seq)` 가 이터레이터를 반환, `next(it)` 로 한 번에 하나씩
- `StopIteration` 예외
- 이터러블 vs 이터레이터: list 는 이터러블, 거기서 iter() 로 만든 게 이터레이터
- 이터레이터는 한 번 소진되면 끝
- Demo: list 의 iter, next 호출

**`02_yield_basics.py`** — yield 와 제너레이터 함수
- `def f(): yield x` — 호출 시 제너레이터 객체 반환
- 호출 시 함수 본문이 즉시 실행되지 않음 (lazy)
- next() 또는 for 로 진행
- `range` 같은 lazy 동작을 직접 구현해본다 (`def my_range(n): ...`)
- Demo: my_range(5) 의 동작

**`03_generator_expressions.py`** — generator expression
- `(x*x for x in range(10))` — 메모리 절약
- sum / max / any / all 같은 함수에 바로 넘기는 패턴
- 비교: 리스트 컴프리헨션 `[x*x for x in range(10)]` 은 전부 메모리에 만든다
- 큰 데이터 처리 시 차이 (개념적으로)
- Demo: 1억까지 합 — generator 로 표현 (실제 실행은 1만 까지만 데모)

**`04_itertools.py`** — itertools 모듈
- `count(start, step)`, `cycle(seq)`, `repeat(x, times)` — 무한/반복
- `chain(a, b)` — 이터러블 연결
- `islice(iter, n)` — 일부만 잘라내기
- `groupby(seq, key)` — 정렬된 데이터 그룹핑 (정렬 필수임을 한 줄)
- `combinations`, `permutations` — 한 줄씩 데모
- Demo: chain + islice 로 무한 카운터에서 10개만 꺼내기

**`05_pipeline.py`** — 제너레이터 파이프라인
- 제너레이터를 다른 제너레이터에 넘겨 데이터 파이프라인 구성
- 예: 파일 줄 읽기 → 빈 줄 필터 → 길이 매핑 → 합산
- 메모리 효율적인 데이터 처리 패턴 — pandas/스트림 처리 전 단계 개념
- Demo: 가짜 데이터 줄 리스트 → 파이프라인 → 결과 한 수

### Exercises (5)

- `ex01_iter_next`: iter([10,20,30]) 만든 뒤 next 3번 호출해 값 확인, 4번째 시도 시 StopIteration 발생 확인 (try/except).
- `ex02_yield_basics`: `even_until(n)` 제너레이터 함수 — 0부터 n 미만 짝수 yield. list 변환 후 검증.
- `ex03_generator_expressions`: generator expression 으로 1~100 제곱의 합 계산.
- `ex04_itertools`: `itertools.chain([1,2], [3,4])` 결과를 list 로, `itertools.islice(itertools.count(0, 2), 5)` 결과 확인.
- `ex05_pipeline`: 주어진 문장 리스트에서 짝수 길이 단어만 골라 대문자로 만든 후 모두 모아 list (제너레이터 체인). assert.

### README

```
# 08_iterators_generators — 이터레이터와 제너레이터

## 배우는 것
- 이터레이터 프로토콜 (iter, next, StopIteration)
- yield 와 제너레이터 함수 — lazy 평가
- generator expression — 메모리 절약
- itertools 의 유용한 도구들
- 제너레이터 파이프라인

## 학습 순서
1. `01_iter_next.py`
2. `02_yield_basics.py`
3. `03_generator_expressions.py`
4. `04_itertools.py`
5. `05_pipeline.py`

## 실행 방법
[bash] uv run python 08_iterators_generators/01_iter_next.py [/bash]

## 연습문제
- `exercises/ex01_*.py` ~ `ex05_*.py` TODO 채우기.
```

### Steps: 같은 7단계.

커밋:
```
git commit -m "feat(08_iterators_generators): iter/yield/genexp/itertools/pipeline — 학습 5 + 연습 5 + 정답 5"
```

---

## Phase 2 종합 검증 (모든 Task 후)

```bash
for d in 05_oop 06_errors_exceptions 07_io_files 08_iterators_generators; do
  for f in $d/0[1-9]_*.py; do
    uv run python "$f" >/dev/null && echo "OK $f" || echo "FAIL $f"
  done
  for f in $d/solutions/ex*.py; do
    out=$(uv run python "$f")
    [ "$out" = "OK" ] && echo "PASS $f" || echo "FAIL $f -> $out"
  done
done
```

---

## Self-Review

**1. 스펙 커버리지:** 05_oop ~ 08_iterators_generators 4 Task로 분담. 각 폴더 학습 5~6 + ex 5~6 + sol 5~6.

**2. Placeholder:** 없음.

**3. 일관성:** 모든 Task가 같은 8 단계.

**4. 모호성:** 각 학습 파일·exercise 마다 다룰 개념 bullet 으로 명시.

---

## 다음 Phase 안내

Phase 2 완료 후 Phase 3 (`09_advanced_python`, `10_typing`, `11_concurrency`) 계획서 작성.
