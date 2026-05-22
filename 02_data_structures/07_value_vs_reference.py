"""
값 타입 vs 참조 타입 — 파이썬의 시각으로.

다른 언어와의 차이점:
- Java/C# 의 "원시(primitive) 타입 vs 참조 타입", JavaScript 의 "primitive vs object" 와 비슷한 구분이 파이썬에도 있다.
- 그런데 파이썬에서는 **모든 것이 객체이고 모든 변수는 참조**다.
  "값 타입처럼 보이는 것"의 정체는 **불변(immutable) 객체** 일 뿐이다 — 변형이 불가능하니 공유돼도 안전.
- 즉, 다른 언어의 "값 vs 참조" ≈ 파이썬의 "**불변 vs 가변**" 으로 읽으면 거의 들어맞는다.
- 이 파일에서 참조 동작의 결과(가변 객체는 공유 시 함께 변한다)를 확인한 뒤,
  다음 파일 `08_copy_immutability.py` 에서 그 함정을 끊는 방법(얕은/깊은 복사, 불변 패턴)으로 이어진다.
"""

# ──── 1. 모든 변수는 "객체를 가리키는 이름표" ────

a = [1, 2, 3]
b = a                            # 새 리스트가 아니다 — a 와 같은 객체에 이름 b 가 추가로 붙는 것뿐
assert a is b                    # `is` — 같은 객체인지 (정체성 비교)
assert id(a) == id(b)            # id() 는 객체의 고유 번호

b.append(4)
assert a == [1, 2, 3, 4]         # 같은 객체를 본 거라 a 쪽에도 변형이 보인다

# ──── 2. `is` 와 `==` 의 차이 ────

x = [1, 2, 3]
y = [1, 2, 3]
assert x == y                    # 값이 같다
assert x is not y                # 그러나 별개 객체

# 결론:
# - 값 비교는 항상 `==`
# - 정체성 비교는 `is` — 거의 항상 `is None` / `is True` / `is False` 검사에만 쓴다

# ──── 3. 불변 객체는 변형 자체가 불가능하다 ────

# 정수·문자열·튜플·frozenset 은 메서드로도 자기 자신을 바꿀 수 없다.
s1 = "hello"
s2 = s1
s1 += " world"                   # 새 문자열 객체를 만들어 s1 이 그쪽을 가리키게 함
assert s2 == "hello"             # s2 는 원래 객체를 그대로 가리킴
# "변형이 보이지 않는다" = 다른 언어의 값 타입 같은 체감

# ──── 4. small int caching — `is` 를 값 비교로 쓰면 안 되는 이유 ────

# CPython 은 자주 쓰는 작은 정수(-5~256)를 캐시해 같은 객체를 재사용한다.
a = 256
b = 256
assert a is b                    # True — 캐시된 같은 객체

# 범위를 벗어나면 같은 값이라도 별개 객체일 수 있다(구현 의존적).
a = 257
b = 257
# `a is b` 는 환경에 따라 True 일 수도 False 일 수도 있다 — 그러니 값 비교에는 절대 쓰지 말 것.
# 값이 같은지 보고 싶다면 항상 `==`.

# ──── 5. 함수 인자 전달 — pass-by-object-reference ────

# 파이썬은 "참조의 값" 이 전달된다고 보면 정확하다.
# - 함수 안에서 객체를 **변형**하면 호출자에게도 보인다(가변 객체일 때).
# - 함수 안에서 매개변수에 **재대입**하면 지역 이름만 바뀌어 호출자에는 영향이 없다.

def grow(lst):
    lst.append(99)               # 변형 — 호출자에게 보임


def rebind(lst):
    lst = lst + [99]             # 재대입 — 지역 이름만 다른 객체를 가리킴


data = [1, 2, 3]
grow(data)
assert data == [1, 2, 3, 99]

data = [1, 2, 3]
rebind(data)
assert data == [1, 2, 3]         # 호출자는 그대로

# ──── 6. 가변 기본 인자 함정 ────

# 기본값은 함수 **정의 시 단 한 번** 평가되어 함수 객체에 붙는다.
# 그래서 가변 객체를 기본값으로 두면 호출 간에 누적된다.
def add_bad(item, bucket=[]):
    bucket.append(item)
    return bucket


_ = add_bad(1)
result = add_bad(2)
assert result == [1, 2]          # 같은 리스트가 호출 사이에 살아남는다 — 거의 항상 버그

# 안전한 패턴: 기본값은 불변 sentinel(None) 로 두고 함수 안에서 새로 만든다.
def add_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


assert add_ok(1) == [1]
assert add_ok(2) == [2]          # 매번 새 리스트

# ──── 7. 정리: "값 vs 참조" 매핑표 ────

# 다른 언어                     | 파이썬에서 같은 체감을 주는 것
# ----------------------------- | -----------------------------
# 원시 타입(int, double, bool)  | 불변 객체 (int, float, bool, str, tuple, frozenset)
# 참조 타입(객체, 배열)         | 가변 객체 (list, dict, set, 일반 클래스 인스턴스)
# 값 복사(pass by value)        | 불변 객체 전달 — 변형 불가라 사실상 값처럼 동작
# 참조 복사(pass by reference)  | 가변 객체 전달 — 변형이 호출자에게 보임

# 이 결과로 생기는 함정 — "참조를 공유하면 가변 객체는 함께 변한다" — 을 끊으려면
# 명시적으로 복사를 해야 한다 → 다음 파일 `08_copy_immutability.py`.

# ──── 8. 다른 언어와의 비교 — Dart / TypeScript ────
#
# (1) 매핑 요약표
#
# 개념                       | Python                            | Dart                                   | TypeScript / JavaScript
# -------------------------- | --------------------------------- | -------------------------------------- | --------------------------------------
# "모든 것이 객체"           | 그렇다                            | 그렇다 (int·bool·String 도 객체)       | 아니다 (primitive vs object 이분)
# 값처럼 동작하는 타입       | 불변 객체 (int, str, tuple, ...)  | 불변 객체 (int, String, ...)           | primitive (number, string, boolean, …)
# 참조처럼 동작하는 타입     | 가변 객체 (list, dict, set, 인스턴스) | List, Map, Set, 사용자 클래스 인스턴스 | object, array, Map, Set, 함수
# 정체성 비교                | `a is b`                          | `identical(a, b)`                      | `a === b` (객체끼리는 같은 객체인지)
# 값 비교                    | `a == b`                          | `a == b` (==/hashCode 오버라이드 필요) | `a === b` (값/타입 동일), 객체는 별도 비교
# 재대입 금지(이름 고정)     | 관례상 UPPER_SNAKE, Final[T] 힌트  | `final x = ...;`                       | `const x = ...;`
# 객체 자체 동결             | `MappingProxyType`, frozen dc      | `List.unmodifiable(...)`, `freezed`    | `Object.freeze(obj)` (얕은 동결)
#
# (2) "대입은 복사가 아니다" — 세 언어에서 같은 동작
#
# Python:
#     a = [1, 2, 3]
#     b = a
#     b.append(4)         # a == [1, 2, 3, 4]
#     assert a is b
#
# Dart:
#     var a = [1, 2, 3];
#     var b = a;
#     b.add(4);                       // a == [1, 2, 3, 4]
#     assert(identical(a, b));        // true
#
# TypeScript:
#     const a: number[] = [1, 2, 3];
#     const b = a;
#     b.push(4);          // a === [1, 2, 3, 4]
#     console.log(a === b); // true
#     // 주의: TS 의 `const` 는 "이름 재대입 금지"일 뿐, 객체 내부 변형은 막지 않는다.
#     //       파이썬의 `Final[T]` 힌트와 의미가 같다.
#
# (3) 정체성 vs 값 비교
#
# Python:        x is y   /   x == y
# Dart:          identical(x, y)   /   x == y      (== 는 클래스에서 오버라이드 가능)
# TypeScript:    x === y                              ← 객체끼리면 정체성, primitive 면 값
#                Object.is(x, y)                      ← NaN·-0 같은 엣지 케이스 포함
#                깊은 값 비교는 표준에 없음 (lodash.isEqual 등 라이브러리 필요)
#
# (4) 함수 인자 전달 — 세 언어 모두 "참조의 값" 전달이라는 동일한 모델
#
# - 함수 안에서 매개변수가 가리키는 **객체를 변형**하면 호출자에게도 보인다.
# - 함수 안에서 매개변수에 **다른 객체를 재대입**하면 호출자에는 보이지 않는다.
# - Java/C# 의 "pass by value of reference" 와 정확히 같은 모델.
#
# (5) 가변 기본 인자 함정 — 파이썬 고유
#
# - 파이썬: 기본값이 **함수 정의 시 한 번** 평가되어 객체에 붙는다 → `def f(x=[]):` 는 거의 항상 버그.
# - Dart: 기본값은 컴파일 타임 상수여야 해서 가변 리터럴을 못 쓴다 → 같은 버그가 컴파일 단계에서 차단된다.
# - TypeScript: 기본값 표현식이 **호출 시점마다** 평가된다 → `function f(x: number[] = []) {}` 안전.
# - 즉 이 함정은 파이썬 학습자가 다른 언어에서 옮겨올 때 가장 자주 밟는 지뢰다.


if __name__ == "__main__":
    # 같은 객체 공유 시연
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(f"a={a}, b={b}, a is b → {a is b}")

    # is vs ==
    x, y = [1, 2, 3], [1, 2, 3]
    print(f"x == y → {x == y}, x is y → {x is y}")

    # 함수 인자 — grow 후 리셋, 그래야 rebind 의 "그대로" 메시지가 명확하다
    data = [1, 2, 3]
    grow(data)
    print(f"grow 후:   {data}  ← 호출자에서도 변형이 보임")
    data = [1, 2, 3]
    rebind(data)
    print(f"rebind 후: {data}  ← 호출자는 그대로")

    # 가변 기본 인자 함정
    print("add_bad(1) →", add_bad(1))
    print("add_bad(2) →", add_bad(2), " ← 누적됨 (버그)")
    print("add_ok(1)  →", add_ok(1))
    print("add_ok(2)  →", add_ok(2), " ← 매번 새 리스트")
