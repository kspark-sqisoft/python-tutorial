"""
구조적 패턴 매칭 — match / case (Python 3.10+, PEP 634).

다른 언어와의 차이점:
- C/Java/Dart 의 `switch` 보다 강하다 — 값뿐 아니라 시퀀스/매핑/객체 구조까지 매칭한다.
- Rust 의 `match`, Scala/Kotlin 의 `when` 과 가장 가까운 모델.
- TypeScript 에는 직접 대응이 없어 학습 가치가 큰 토픽이다.
- 식별자(소문자)는 "캡처"로 동작 — `case x:` 는 모든 값에 매치되며 x 에 캡처된다.
  상수와 비교하려면 점이 포함된 이름(`Color.RED`)을 쓰거나 가드를 사용한다.
- `match` 는 문(statement)이지 식(expression)이 아니므로, 결과를 받으려면 함수 안 `return` 또는 일반 대입을 쓴다.
- 자세한 언어 비교는 파일 끝 섹션.
"""

from dataclasses import dataclass
from enum import Enum, auto


# ──── 1. 리터럴 + OR + 와일드카드 ────

def http_label(code: int) -> str:
    match code:
        case 200:                 return "OK"
        case 301 | 302:           return "Redirect"
        case 404:                 return "Not Found"
        case 500 | 502 | 503:     return "Server Error"
        case _:                   return "Unknown"


assert http_label(200) == "OK"
assert http_label(302) == "Redirect"
assert http_label(503) == "Server Error"
assert http_label(418) == "Unknown"


# ──── 2. 시퀀스 패턴 — list/tuple 모두 가능 ────

def head_tail(seq):
    match seq:
        case []:               return "empty"
        case [only]:           return f"single: {only}"
        case [a, b]:           return f"pair: {a}, {b}"
        case [first, *rest]:   return f"first={first}, rest={rest}"


assert head_tail([]) == "empty"
assert head_tail([7]) == "single: 7"
assert head_tail([1, 2]) == "pair: 1, 2"
assert head_tail([1, 2, 3, 4]) == "first=1, rest=[2, 3, 4]"


# ──── 3. 매핑 패턴 — 필요한 키만 매칭 ────

def event_kind(event: dict) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click@({x},{y})"
        case {"type": "key", "name": name}:
            return f"key:{name}"
        case {"type": t}:                       # 알려진 키만 보고 나머지는 무시
            return f"unknown:{t}"
        case _:
            return "no type"


assert event_kind({"type": "click", "x": 10, "y": 20, "ts": 999}) == "click@(10,20)"
assert event_kind({"type": "key", "name": "Enter"}) == "key:Enter"
assert event_kind({"type": "scroll"}) == "unknown:scroll"
assert event_kind({}) == "no type"


# ──── 4. 클래스 패턴 — 위치/키워드 인자 모두 가능 ────

@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    center: Point
    radius: float


def describe(shape) -> str:
    match shape:
        case Point(x=0, y=0):           return "원점"
        case Point(x=0, y=y):           return f"y축 위 {y}"
        case Point(x=x, y=0):           return f"x축 위 {x}"
        case Point():                   return "임의의 점"      # 모든 Point 매치
        case Circle(center=Point(0, 0), radius=r):
            return f"원점 중심 반지름 {r}"
        case Circle(center=c, radius=r):
            return f"중심 {c} 반지름 {r}"
        case _:
            return "기타"


assert describe(Point(0, 0)) == "원점"
assert describe(Point(0, 5)) == "y축 위 5"
assert describe(Point(3, 0)) == "x축 위 3"
assert describe(Point(3, 4)) == "임의의 점"
assert describe(Circle(Point(0, 0), 3.0)) == "원점 중심 반지름 3.0"
assert describe(Circle(Point(1, 2), 4.0)) == "중심 Point(x=1, y=2) 반지름 4.0"


# ──── 5. 가드(if) — 패턴 + 추가 조건 ────

def sign_label(n: int) -> str:
    match n:
        case 0:                  return "zero"
        case x if x > 0:         return "positive"
        case x if x < 0:         return "negative"


assert sign_label(0) == "zero"
assert sign_label(5) == "positive"
assert sign_label(-3) == "negative"


# ──── 6. 캡처 vs 상수 — 가장 자주 밟는 함정 ────

class Color(Enum):
    RED = auto()
    BLUE = auto()


def color_name(c) -> str:
    match c:
        # ❌ `case RED:` 라고 쓰면 RED 라는 "이름으로 모든 값을 캡처" 해버려 항상 첫 case 가 잡힌다.
        # ⭕ 점이 포함된 이름(`Color.RED`)은 상수로 해석된다.
        case Color.RED:   return "red"
        case Color.BLUE:  return "blue"
        case _:           return "unknown"


assert color_name(Color.RED) == "red"
assert color_name(Color.BLUE) == "blue"


# ──── 7. 시퀀스 안의 클래스 패턴 — 강력한 조합 ────

def first_two_points(items) -> str:
    match items:
        case [Point(0, 0), Point(x, y), *_]:
            return f"원점 다음 → ({x}, {y})"
        case [Point() as p1, Point() as p2, *_]:
            return f"두 점: {p1}, {p2}"
        case _:
            return "매치 안 됨"


assert first_two_points([Point(0, 0), Point(3, 4), Point(9, 9)]) == "원점 다음 → (3, 4)"


# ──── 8. 다른 언어와의 비교 — Dart / TypeScript ────
#
# 작업                          | Python (match)                       | Dart 3 (switch expression)              | TypeScript
# ----------------------------- | ------------------------------------ | --------------------------------------- | ---------------------------------------------
# 리터럴 + OR                   | `case 1 | 2 | 3:`                    | `case 1 || 2 || 3 =>`                   | switch-case (또는 `Set` 멤버십)
# 시퀀스 분해                   | `case [a, b, *rest]:`                | `case [var a, var b, ...var rest] =>`   | tuple 타입 + narrowing (불완전)
# 매핑(부분) 매칭               | `case {"type": "click", "x": x}:`    | (직접 if-else 로 분기)                  | discriminated union + narrowing
# 클래스 분해                   | `case Point(x=0, y=y):`              | `case Point(:final x, y: 0) =>`         | discriminated union (`{ kind: "point", x, y }`)
# 가드                          | `case x if x > 0:`                   | `case var x when x > 0 =>`              | switch 안에서 if (가독성 떨어짐)
# 캡처                          | 소문자 식별자 자동 캡처              | `var x` 또는 `:final x`                 | discriminated narrowing 시 자동
# 직접 대응 부재                | —                                    | —                                       | **없음** (TS 에 가장 부족한 기능 중 하나)
#
# 핵심 차이
# - Dart 3 의 patterns(2023) 가 파이썬 match 와 가장 비슷한 표현력을 가진다.
# - TS 에는 패턴 매칭이 없어 `ts-pattern` 같은 라이브러리로 보완 — 파이썬 match 가 가장 큰 비교 가치.
# - Rust 의 exhaustiveness 검사(컴파일러가 모든 케이스를 강제)는 파이썬에 없다 — `case _` 를 직접 챙겨야 한다.


if __name__ == "__main__":
    print("=== http_label ===")
    for c in (200, 302, 404, 503, 418):
        print(f"  {c} → {http_label(c)}")

    print("\n=== head_tail ===")
    for seq in ([], [1], [1, 2], [1, 2, 3, 4]):
        print(f"  {seq} → {head_tail(seq)}")

    print("\n=== event_kind ===")
    for ev in (
        {"type": "click", "x": 10, "y": 20},
        {"type": "key", "name": "Enter"},
        {"type": "scroll"},
        {},
    ):
        print(f"  {ev} → {event_kind(ev)}")

    print("\n=== describe (클래스 패턴) ===")
    for shape in (Point(0, 0), Point(0, 5), Point(3, 4), Circle(Point(0, 0), 3.0)):
        print(f"  {shape} → {describe(shape)}")

    print("\n=== sign_label (가드) ===")
    for n in (0, 5, -3):
        print(f"  {n} → {sign_label(n)}")
