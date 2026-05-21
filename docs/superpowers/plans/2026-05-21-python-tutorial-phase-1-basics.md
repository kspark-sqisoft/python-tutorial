# Python Tutorial — Phase 1 (기초) 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Phase 1 네 개 폴더(`01_basics`, `02_data_structures`, `03_functions`, `04_modules_packages`)에 학습 스크립트·연습문제·정답을 채우고, 각 폴더 README를 placeholder에서 실제 안내로 교체한다.

**Architecture:** 폴더 단위로 한 서브에이전트가 작업한다. 각 폴더의 모든 학습 스크립트 + `exercises/` TODO + `solutions/` 정답을 한 묶음으로 작성한다. 작업 후 폴더 안의 모든 학습 스크립트와 정답 스크립트를 실행해 무오류로 돌아가는지 확인하고, 폴더 단위로 커밋한다.

**Tech Stack:** Python 3.12, 표준 라이브러리만. 외부 라이브러리는 사용하지 않는다.

**참조 스펙:** `docs/superpowers/specs/2026-05-21-python-tutorial-design.md`
**선행 계획:** Phase 0 (`docs/superpowers/plans/2026-05-21-python-tutorial-phase-0-skeleton.md`) 완료 — git commit `24b04ab`.

---

## 모든 파일에 강제되는 스타일 규칙 (스펙 §2.3, §2.4)

학습 스크립트 (`NN_topic.py`)는 다음을 반드시 따른다.

1. **상단 docstring**: 다루는 개념·다른 언어와의 차이를 3~5줄 요약.
2. **`# ──── 번호. 소제목 ────` 구분선** (정확히 4개의 박스 라인 문자 `─` 사용. 유니코드 U+2500).
3. **개념 첫 등장 시 줄 단위 한국어 주석**, 반복되는 부분은 생략 (노이즈 방지).
4. **파일 끝 `if __name__ == "__main__":` 데모 블록** — 의미 있는 출력을 낸다.
5. **식별자는 영어 (snake_case), 주석·문자열은 한국어**.
6. **외부 라이브러리·타입 힌트·class·예외처리 사용 금지** (Phase 1은 절차적 기초). 단, `04_modules_packages`는 표준 라이브러리 import 허용.

연습문제 (`exercises/exNN_*.py`)는 다음을 따른다.

1. 상단 docstring으로 무엇을 풀어야 하는지·어떻게 실행하는지 명시.
2. `TODO N:` 주석으로 채울 자리를 표시. 값은 `...` 또는 `None`으로 둔다.
3. 파일 끝에 `assert` 자가 채점. 다 채우면 `print("OK")` 출력.
4. **정답 없이 그대로 실행하면 `AssertionError` 또는 `TypeError`로 실패해야 한다.**

정답 (`solutions/exNN_*.py`)는 다음을 따른다.

1. 같은 파일 이름.
2. 상단 docstring에 "왜 이렇게 풀었나" 한 문단.
3. 실행 시 `OK`만 출력 (assert 통과).

---

## Task 1: `01_basics/` — 기초 자료형과 제어흐름

**Files:**
- Modify: `01_basics/README.md` (placeholder → 실제 내용)
- Create: `01_basics/01_variables.py`
- Create: `01_basics/02_numbers.py`
- Create: `01_basics/03_strings.py`
- Create: `01_basics/04_booleans.py`
- Create: `01_basics/05_control_flow.py`
- Create: `01_basics/06_io.py`
- Create: `01_basics/exercises/ex01_variables.py` ~ `ex06_io.py` (6개)
- Create: `01_basics/solutions/ex01_variables.py` ~ `ex06_io.py` (6개)

### 각 학습 스크립트의 다뤄야 할 개념

**`01_variables.py`** — 변수·동적 타이핑
- 변수 = 객체에 붙인 이름표 모델 설명
- 다른 언어와의 차이: 타입 선언 없음, 재대입 시 타입 변경 가능
- `id()`로 같은 객체 가리키기 보이기
- `del` 로 이름표 떼기
- 튜플 언패킹 (`x, y = 1, 2`), 체인 대입(`a = b = 0`)
- 데모: 변수 3~4개 만들고 type/id 출력

**`02_numbers.py`** — 숫자와 연산자
- `int` (임의 정밀도 — 다른 언어와의 큰 차이), `float`, `complex` (간단히만)
- 사칙연산, `**` 거듭제곱, `//` 정수 나눗셈, `%` 나머지
- `divmod(a, b)`
- 정수 ↔ float 변환, `round()`, `abs()`
- 진법 표기 `0b`, `0o`, `0x`
- 데모: 큰 수 거듭제곱(예: `2 ** 100`)으로 임의 정밀도 시연

**`03_strings.py`** — 문자열
- 작은따옴표/큰따옴표/삼중따옴표 동등성
- f-string (`{name}`, `{value!r}`, `{x:.2f}`, `{n:>5}`)
- 자주 쓰는 메서드: `upper`, `lower`, `strip`, `split`, `join`, `replace`, `startswith`, `endswith`, `find`, `count`
- 인덱싱과 슬라이싱 (`s[0]`, `s[-1]`, `s[1:4]`, `s[::-1]`)
- 문자열은 불변 — `s[0] = 'x'`가 안 됨을 주석으로 명시
- 데모: 이름·문장에 위 기능 적용

**`04_booleans.py`** — 불리언과 truthy/falsy
- `True`/`False` (첫 자 대문자 — 다른 언어와의 차이)
- 비교 연산자 `==`, `!=`, `<`, `>=`, `is`, `is not`, `in`, `not in`
- `==` vs `is` 차이 (값 비교 vs 동일 객체)
- truthy/falsy 규칙: 빈 컬렉션·0·None·"" 은 False, 나머지는 True
- 단락 평가 (`and`, `or` 의 값 반환 — C와 다른 점)
- 데모: `1 < x < 10` 체인 비교, 단락 평가로 기본값 패턴

**`05_control_flow.py`** — 제어흐름
- `if / elif / else`
- `while` (`break`, `continue`, `else`(루프) 한 줄 설명)
- `for` (`range`, `enumerate`, `zip` 간단 소개)
- `match` (Python 3.10+ 패턴 매칭) — 간단 예제만
- 데모: FizzBuzz 또는 그에 준하는 짧은 예제

**`06_io.py`** — 표준 입출력과 포맷팅
- `print(*args, sep=, end=)` — `sep`, `end` 키워드 인자
- `input(prompt)` — 항상 str 반환, 변환 필요
- `f-string` 정렬 (`:<`, `:>`, `:^`, `:0>3`)
- 데모: `input` 은 비대화 환경에서 막히므로 데모에선 **사용하지 않는다**. 대신 `print` 옵션과 f-string 포맷팅만 시연.
- 주석으로 "실제 입력은 다음과 같이 받는다" 코드 예제만 보여준다.

### 연습문제 6개 (예시 패턴)

각 연습문제는 짧고 한 가지 개념만 묻는다.

- `ex01_variables.py`: 정수 `age=30`, 문자열 `name="Kee"` 두 변수를 만들고, 튜플 언패킹으로 동시 대입한 `(a, b) = ...` 도 채우게 한다.
- `ex02_numbers.py`: `2**10` 계산, `divmod(17, 5)` 결과 검증.
- `ex03_strings.py`: 문자열 슬라이싱과 메서드 (`split`, `join`).
- `ex04_booleans.py`: truthy/falsy 판정 (`bool(0)`, `bool("False")` 등을 `expected` 와 비교).
- `ex05_control_flow.py`: 1~20 까지 짝수만 모아 리스트로 반환 (for + if).
- `ex06_io.py`: f-string 으로 표 한 줄 만들기 (예: `"이름: Kee   | 점수: 95"`)

### Steps

- [ ] **Step 1: 폴더 안 모든 학습 스크립트 6개 작성**

스타일 규칙을 따라 위 6개 파일을 작성한다.

- [ ] **Step 2: `exercises/` 폴더 만들고 6개 ex 파일 작성**

`mkdir -p 01_basics/exercises 01_basics/solutions`

각 ex 파일은 정답 미작성 상태로 실행 시 실패해야 한다.

- [ ] **Step 3: `solutions/` 폴더에 6개 정답 파일 작성**

정답은 실행 시 `OK` 만 출력.

- [ ] **Step 4: README 교체**

`01_basics/README.md` 의 placeholder를 실제 내용으로 교체. 4단 구성 유지:

```
# 01_basics — 기초 자료형과 제어흐름

## 배우는 것
- 변수와 동적 타이핑 (객체에 붙인 이름표)
- 숫자(int 임의 정밀도 포함), 문자열, 불리언
- truthy/falsy 규칙
- if/while/for/match 제어흐름
- print/f-string 출력 포맷팅

## 학습 순서
1. `01_variables.py`
2. `02_numbers.py`
3. `03_strings.py`
4. `04_booleans.py`
5. `05_control_flow.py`
6. `06_io.py`

## 실행 방법
` ` `bash
uv run python 01_basics/01_variables.py
` ` `

## 연습문제
- `exercises/ex01_variables.py` ~ `ex06_io.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 같은 번호 파일과 비교.
```

(위 ` ` ` 는 실제 ``` 로 작성)

- [ ] **Step 5: 모든 학습 스크립트 실행 검증**

```bash
for f in 01_basics/0[1-6]_*.py; do
  echo "--- $f ---"
  uv run python "$f" || echo "FAIL: $f"
done
```
Expected: 6 파일 모두 무오류 실행, 각각 의미 있는 출력.

- [ ] **Step 6: 모든 정답 실행 검증 ('OK' 출력 확인)**

```bash
for f in 01_basics/solutions/ex0[1-6]_*.py; do
  out=$(uv run python "$f")
  if [ "$out" = "OK" ]; then
    echo "PASS $f"
  else
    echo "FAIL $f -> $out"
  fi
done
```
Expected: 6 파일 모두 `PASS`.

- [ ] **Step 7: 빈 exercise 가 실패하는지 확인 (샘플 2개)**

```bash
uv run python 01_basics/exercises/ex01_variables.py || echo "ex01 정상적으로 실패"
uv run python 01_basics/exercises/ex05_control_flow.py || echo "ex05 정상적으로 실패"
```
Expected: 두 명령 모두 실패(0 아닌 종료 코드)하고 메시지 출력.

- [ ] **Step 8: 폴더 단위 커밋**

```bash
git add 01_basics/
git commit -m "feat(01_basics): 기초 자료형과 제어흐름 — 학습 스크립트 6 + 연습 6 + 정답 6"
```

---

## Task 2: `02_data_structures/` — 자료구조

**Files:**
- Modify: `02_data_structures/README.md`
- Create: `02_data_structures/01_list.py`
- Create: `02_data_structures/02_tuple.py`
- Create: `02_data_structures/03_dict.py`
- Create: `02_data_structures/04_set.py`
- Create: `02_data_structures/05_comprehensions.py`
- Create: `02_data_structures/06_slicing.py`
- Create: `02_data_structures/exercises/ex01_list.py` ~ `ex06_slicing.py`
- Create: `02_data_structures/solutions/ex01_list.py` ~ `ex06_slicing.py`

### 각 학습 스크립트의 다뤄야 할 개념

**`01_list.py`** — list (가변 시퀀스)
- 생성: `[]`, `list()`, `list(range(5))`
- 인덱싱·슬라이싱
- 변경 메서드: `append`, `extend`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`
- 비파괴 작업: `sorted`, `reversed`, `[1, 2] + [3]`, `[0] * 5`
- 중첩 리스트 (2D)
- 주의: 가변 객체이므로 `b = a` 는 같은 객체를 가리킨다 (얕은 복사 vs 깊은 복사 한 줄)
- 데모: 리스트 만들고 정렬·필터링.

**`02_tuple.py`** — tuple (불변 시퀀스)
- 생성: `(1, 2, 3)`, `1, 2, 3`, `tuple([...])`, 단일 요소 `(1,)` 주의
- 인덱싱/슬라이싱 (list와 동일)
- 불변 — 메서드는 `count`, `index` 만
- 언패킹 (`a, b, c = t`), 별표 언패킹 (`first, *rest = ...`)
- 함수 반환값으로 자주 쓰이는 이유
- 데모: divmod 같은 다중 반환 받기

**`03_dict.py`** — dict (해시맵)
- 생성: `{}`, `dict(a=1, b=2)`, `dict([("a", 1)])`
- 접근: `d["k"]`, `d.get("k", default)`, `"k" in d`
- 변경: `d["k"] = v`, `d.update({...})`, `del d["k"]`, `d.pop`
- 순회: `for k in d`, `d.keys`, `d.values`, `d.items`
- 정렬은 안 되지만 3.7+ 부터 삽입 순서 유지
- 데모: 단어 빈도 세기 (5 단어 정도)

**`04_set.py`** — set (집합)
- 생성: `set()` (빈 set), `{1, 2, 3}`, `set([1, 1, 2])` 중복 제거
- 추가/제거: `add`, `discard`, `remove`
- 집합 연산: `&`, `|`, `-`, `^` (교/합/차/대칭차)
- 가입 검사 `in` 이 O(1) — list와 비교
- `frozenset` 은 한 줄 언급
- 데모: 두 리스트의 공통 원소 찾기

**`05_comprehensions.py`** — 컴프리헨션
- list/dict/set/generator 컴프리헨션
- 기본 형식: `[expr for x in seq]`, 조건: `[expr for x in seq if cond]`
- 중첩: `[(x, y) for x in xs for y in ys]`
- dict 컴프리헨션: `{k: v for k, v in pairs}`
- generator 컴프리헨션: `(x*x for x in range(10))` — 메모리 절약
- 데모: 한 줄로 단어 길이 매핑 dict 만들기

**`06_slicing.py`** — 슬라이싱 종합
- `seq[start:stop:step]` 의미 (stop은 미포함)
- 음수 인덱스/스텝
- 전체 복사 `seq[:]`
- 거꾸로 `seq[::-1]`
- list/tuple/str/range 모두 동일 슬라이싱
- 슬라이스로 부분 변경 `lst[1:3] = [...]` (list 전용)
- 데모: 다양한 슬라이스 결과 출력

### 연습문제 6개 (개념)

- `ex01_list`: 1~10 리스트 생성, 짝수만 새 리스트
- `ex02_tuple`: 좌표 점 5개 튜플 정렬 (`sorted(key=...)`)
- `ex03_dict`: 주어진 문장의 단어 빈도 dict
- `ex04_set`: 두 리스트의 합집합·교집합·차집합 각각
- `ex05_comprehensions`: 컴프리헨션으로 구구단 dict `{(i,j): i*j}`
- `ex06_slicing`: 슬라이싱으로 문자열 회문 검사 함수 없이 직접

### Steps

- [ ] **Step 1~7: Task 1과 동일한 절차** (학습 6 + ex 6 + sol 6 작성, 모두 실행 검증)

- [ ] **Step 8: 커밋**

```bash
git add 02_data_structures/
git commit -m "feat(02_data_structures): list/tuple/dict/set/컴프리헨션/슬라이싱 — 학습 6 + 연습 6 + 정답 6"
```

---

## Task 3: `03_functions/` — 함수

**Files:**
- Modify: `03_functions/README.md`
- Create: `03_functions/01_function_basics.py`
- Create: `03_functions/02_args_kwargs.py`
- Create: `03_functions/03_lambda_higher_order.py`
- Create: `03_functions/04_scope_closure.py`
- Create: `03_functions/05_recursion.py`
- Create: `03_functions/exercises/ex01_*.py` ~ `ex05_*.py` (5개)
- Create: `03_functions/solutions/ex01_*.py` ~ `ex05_*.py` (5개)

### 각 학습 스크립트의 다뤄야 할 개념

**`01_function_basics.py`** — 함수 기본
- `def name(args):` / `return`
- 기본 인자 `def f(x, y=10)`
- 기본 인자의 함정: 가변 기본 인자(`def f(x, lst=[])`) 절대 쓰지 말 것 (예제로 동작 보여주기)
- 키워드 인자로 호출
- docstring (`"""..."""`) 첫 문장 = 한 줄 요약, `help(f)` 로 보임
- 데모: 간단한 add 함수, 인사 함수

**`02_args_kwargs.py`** — 가변 인자
- `*args` (튜플로 모임)
- `**kwargs` (dict로 모임)
- 호출 시 언패킹: `f(*lst)`, `f(**d)`
- 키워드 전용 매개변수: `def f(a, *, b)` — b는 키워드로만
- 위치 전용 매개변수: `def f(a, /, b)` — 간단히만
- 데모: 인자 출력기 만들기

**`03_lambda_higher_order.py`** — 람다와 고차함수
- `lambda x: x*x` — 짧은 함수 표현
- `sorted(seq, key=lambda x: ...)`, `max`, `min` 의 key
- `map`, `filter` 와 컴프리헨션 비교 (보통 컴프리헨션이 더 파이썬다움)
- 함수도 변수에 담을 수 있다 (1급 객체)
- 데모: 이름 리스트를 성씨 길이로 정렬

**`04_scope_closure.py`** — 스코프와 클로저
- LEGB 규칙 (Local, Enclosing, Global, Built-in)
- `global`, `nonlocal` 키워드 (각각 한 예제)
- 클로저: 함수가 자신을 둘러싼 변수를 캡처
- 데모: 카운터 함수(`make_counter`) 클로저로 만들기

**`05_recursion.py`** — 재귀
- 기본 패턴: 종료조건 + 자기 호출
- 예제: 팩토리얼, 피보나치 (느린 버전)
- 파이썬의 재귀 한계: `sys.getrecursionlimit()` (보통 1000) — 다른 언어와 다른 부분
- 꼬리 재귀 최적화 없음 — 큰 입력은 반복문 권장
- 데모: factorial(10), fib(10)

### 연습문제 5개

- `ex01_function_basics`: 절댓값 함수 `abs_value` 작성, 기본인자 활용
- `ex02_args_kwargs`: `*args` 합 함수, `**kwargs` 를 키 정렬 출력
- `ex03_lambda_higher_order`: 사람 리스트를 나이 키로 정렬
- `ex04_scope_closure`: `make_adder(n)` 클로저로 덧셈기 만들기
- `ex05_recursion`: 리스트 깊이 합 (중첩 리스트 재귀 합산)

### Steps

Task 1과 동일 (Step 1~7 작성·검증, Step 8 커밋).

```bash
git commit -m "feat(03_functions): 함수 기본/가변인자/람다/스코프/재귀 — 학습 5 + 연습 5 + 정답 5"
```

---

## Task 4: `04_modules_packages/` — 모듈과 패키지

**Files:**
- Modify: `04_modules_packages/README.md`
- Create: `04_modules_packages/01_import_basics.py`
- Create: `04_modules_packages/02_stdlib_pathlib.py`
- Create: `04_modules_packages/03_stdlib_datetime.py`
- Create: `04_modules_packages/04_stdlib_random_math.py`
- Create: `04_modules_packages/05_making_modules.py` (호출자)
- Create: `04_modules_packages/mypkg/__init__.py`
- Create: `04_modules_packages/mypkg/greet.py`
- Create: `04_modules_packages/mypkg/calc.py`
- Create: `04_modules_packages/exercises/ex01_*.py` ~ `ex05_*.py`
- Create: `04_modules_packages/solutions/ex01_*.py` ~ `ex05_*.py`

### 각 학습 스크립트의 다뤄야 할 개념

**`01_import_basics.py`** — import 4가지 형태
- `import math`
- `from math import sqrt, pi`
- `import math as m`
- `from math import sqrt as 제곱근` (이렇게도 됨, 권장은 안 함)
- import 의 위치: 파일 상단이 관례
- `__name__ == "__main__":` 가 왜 import 시 실행 안 되는지 다시 설명
- 데모: 4가지 방식으로 sqrt 호출

**`02_stdlib_pathlib.py`** — `pathlib`
- `Path(__file__)`, `Path.cwd()`, `Path.home()`
- 경로 결합 `p / "sub" / "file.txt"`
- `.exists()`, `.is_file()`, `.is_dir()`, `.suffix`, `.stem`, `.name`, `.parent`
- 디렉터리 순회 `list(p.iterdir())`, `p.glob("*.py")`
- 데모: 자기 자신 파일의 부모·이름·확장자 출력 (`Path(__file__).parent`)

**`03_stdlib_datetime.py`** — `datetime`
- `from datetime import datetime, date, time, timedelta`
- `datetime.now()`, `date.today()`
- `strftime("%Y-%m-%d %H:%M")`, `strptime(...)`
- 산술: `datetime.now() + timedelta(days=7)`
- 시간대(`timezone.utc`) 한 줄
- 데모: 오늘 날짜, 일주일 후, 100일 후 출력

**`04_stdlib_random_math.py`** — `random`, `math`
- `random.random`, `random.randint`, `random.choice`, `random.sample`, `random.shuffle`
- 시드: `random.seed(42)` 로 재현 가능
- `math.pi`, `math.e`, `math.sqrt`, `math.floor`, `math.ceil`, `math.log`
- 데모: seed 42로 5개 뽑기 (재현성 보장)

**`05_making_modules.py`** — 자체 패키지 만들기
- `mypkg/__init__.py` 의 역할 (한 줄 docstring 정도)
- `mypkg/greet.py` 에 `hello(name)`, `mypkg/calc.py` 에 `add(a, b)` 정의
- 호출자(05번)에서 `from mypkg.greet import hello`, `from mypkg.calc import add` 사용
- 데모: hello("파이썬"), add(2, 3) 출력

**`mypkg/__init__.py`** — 빈 docstring 한 줄
```python
"""학습용 미니 패키지."""
```

**`mypkg/greet.py`** —
```python
"""인사 함수 모듈."""

def hello(name):
    """입력 받은 이름으로 인사 문자열을 만들어 반환한다."""
    return f"안녕하세요, {name} 님!"
```

**`mypkg/calc.py`** —
```python
"""간단한 산술 함수."""

def add(a, b):
    """두 수를 더해서 반환."""
    return a + b
```

### 연습문제 5개

- `ex01_import_basics`: 표준 `math` 에서 `sqrt`, `pi` 를 import 해서 원의 둘레 계산
- `ex02_pathlib`: 현재 파일의 디렉터리 경로를 Path 로 얻기
- `ex03_datetime`: 오늘 + 30일 후 날짜 문자열
- `ex04_random_math`: seed(7) 로 randint(1, 100) 3번 호출 → 고정된 값 검증
- `ex05_making_modules`: `mypkg.calc.add` 와 `mypkg.greet.hello` 직접 호출 (정답에선 import 추가, exercise 에선 import TODO)

### Steps

- [ ] **Step 1: 학습 스크립트 5개 + mypkg 3개 파일 작성**

- [ ] **Step 2~3: exercises/, solutions/ 5개씩 작성**

- [ ] **Step 4: README 교체**

- [ ] **Step 5: 학습 스크립트 5개 실행 검증**

```bash
for f in 04_modules_packages/0[1-5]_*.py; do
  echo "--- $f ---"
  uv run python "$f" || echo "FAIL: $f"
done
```

- [ ] **Step 6: 정답 5개 실행 검증**

```bash
for f in 04_modules_packages/solutions/ex0[1-5]_*.py; do
  out=$(uv run python "$f")
  [ "$out" = "OK" ] && echo "PASS $f" || echo "FAIL $f -> $out"
done
```

- [ ] **Step 7: 빈 exercise 실패 검증 (샘플)**

```bash
uv run python 04_modules_packages/exercises/ex05_making_modules.py || echo "정상 실패"
```

- [ ] **Step 8: 커밋**

```bash
git add 04_modules_packages/
git commit -m "feat(04_modules_packages): import 4형/표준 라이브러리(pathlib/datetime/random/math)/자체 패키지 — 학습 5 + 연습 5 + 정답 5"
```

---

## Phase 1 종합 검증 (마지막 Task 후)

- [ ] **모든 폴더 스크립트 일괄 실행**

```bash
for d in 01_basics 02_data_structures 03_functions 04_modules_packages; do
  for f in $d/0[1-9]_*.py; do
    uv run python "$f" >/dev/null && echo "OK $f" || echo "FAIL $f"
  done
done
```
Expected: 모든 줄이 `OK` 로 시작.

- [ ] **모든 정답 일괄 실행**

```bash
for d in 01_basics 02_data_structures 03_functions 04_modules_packages; do
  for f in $d/solutions/ex*.py; do
    out=$(uv run python "$f")
    [ "$out" = "OK" ] && echo "PASS $f" || echo "FAIL $f"
  done
done
```
Expected: 모든 줄이 `PASS` 로 시작.

---

## Self-Review

**1. 스펙 커버리지:**
- [x] §2.3 주석 4원칙 / §2.4 파일 스타일 — Steps 머리에 명시
- [x] §3 폴더 구조 (01~04) — 4 Task로 분담
- [x] §4 README 4단 템플릿 — 각 Task Step 4
- [x] §5 연습문제 형식 (assert 자가 채점) — 각 Task에 명시

**2. Placeholder:** 없음. "(Phase N에서 채워짐)" 자리는 Task Step 4에서 실제 내용으로 교체됨.

**3. 일관성:** 모든 Task가 같은 8 Step 패턴(작성→exercises→solutions→README→학습검증→정답검증→실패검증→커밋).

**4. 모호성:** 각 .py 마다 "다뤄야 할 개념" 항목을 bullet으로 고정 — 서브에이전트가 임의로 범위 확장 못 함.

---

## 다음 Phase 안내

Phase 1 완료 후 Phase 2 계획서를 별도 파일로 작성:
`docs/superpowers/plans/<date>-python-tutorial-phase-2-intermediate.md`
Phase 2 범위: `05_oop`, `06_errors_exceptions`, `07_io_files`, `08_iterators_generators`.
