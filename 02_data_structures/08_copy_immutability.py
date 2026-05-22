"""
얕은 복사(shallow copy) vs 깊은 복사(deep copy), 그리고 불변성 유지 패턴.

선행: `07_value_vs_reference.py` 에서 "대입은 같은 객체에 이름만 추가하는 것"임을 확인했다.
이 파일은 그 결과로 생기는 "참조 공유로 인한 의도치 않은 변형" 함정을 끊는 도구들을 다룬다.

다른 언어와의 차이점:
- Java 의 `clone()`, Dart 의 `List.from`/`[...other]`, JavaScript 의 `Object.assign`/스프레드와 비슷하게,
  파이썬도 명시적으로 복사를 요청해야 한다 — `list.copy()`, `dict.copy()`, `copy.copy()` 모두 얕은 복사다.
- 중첩 객체까지 완전히 분리하려면 표준 라이브러리 `copy.deepcopy()` 가 필요하다.
  TypeScript 의 `structuredClone()`, Dart 의 `jsonDecode(jsonEncode(...))` 트릭과 같은 위치의 도구.
- 불변(immutable) 객체(int, str, tuple, frozenset, frozen dataclass)는 복사가 사실상 무의미하다 — 공유해도 안전.
- 자세한 언어 간 매핑은 파일 끝의 "다른 언어와의 비교" 섹션 참고.
"""

import copy
from dataclasses import dataclass
from types import MappingProxyType

# ──── 1. 대입은 복사가 아니다 ────

a = [1, 2, 3]
b = a                       # 같은 리스트를 가리키는 또 다른 이름일 뿐
b.append(4)
# a 도 [1, 2, 3, 4] — 둘은 같은 객체
assert a is b
assert a == [1, 2, 3, 4]

# ──── 2. 얕은 복사 — 최상위만 새로 만든다 ────

# list 의 얕은 복사 방법 4가지 (모두 동치)
original = [1, 2, 3]
s1 = original.copy()        # 메서드
s2 = list(original)         # 생성자
s3 = original[:]            # 슬라이스
s4 = copy.copy(original)    # copy 모듈

assert s1 == s2 == s3 == s4 == [1, 2, 3]
assert s1 is not original   # 다른 객체

# 평탄(flat) 리스트라면 얕은 복사로 충분
s1.append(99)
assert original == [1, 2, 3]  # 원본은 영향 없음

# ──── 3. 얕은 복사의 함정 — 중첩 객체는 공유된다 ────

nested = [[1, 2], [3, 4]]
shallow = nested.copy()         # 바깥 리스트만 새로 만든다
# 안쪽 리스트는 여전히 nested 와 같은 객체를 가리킨다
assert shallow[0] is nested[0]

shallow[0].append(999)
# 원본까지 변형됨 — 흔히 디버깅 시간을 잡아먹는 함정
assert nested == [[1, 2, 999], [3, 4]]

# ──── 4. 깊은 복사 — 재귀적으로 전부 새로 만든다 ────

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
assert deep[0] is not nested[0]   # 안쪽까지 별개 객체

deep[0].append(999)
assert nested == [[1, 2], [3, 4]]  # 원본 보존

# 깊은 복사는 객체 그래프를 따라가며 모든 노드를 재생성하므로 비용이 크다.
# 평탄한 구조에는 쓰지 말고, 중첩이 있는 경우에만 선택한다.

# ──── 5. dict 도 동일한 함정 ────

settings = {"db": {"host": "localhost", "port": 5432}, "debug": True}

shallow_cfg = settings.copy()        # 또는 dict(settings), {**settings}
shallow_cfg["db"]["host"] = "remote"
# 원본 settings 의 db.host 까지 바뀐다
assert settings["db"]["host"] == "remote"

settings["db"]["host"] = "localhost"  # 되돌리고
deep_cfg = copy.deepcopy(settings)
deep_cfg["db"]["host"] = "remote"
assert settings["db"]["host"] == "localhost"  # 이번엔 원본 안전

# ──── 6. 불변 객체는 복사가 필요 없다 ────

# int, str, tuple, frozenset 은 값을 바꿀 수 없으므로 공유해도 안전하다.
t1 = (1, 2, 3)
t2 = t1            # 같은 객체를 가리켜도 누구도 변형할 수 없음
assert t1 is t2

# 단, "튜플이 불변" ≠ "안에 든 리스트가 불변" — 튜플 안에 가변 객체를 담으면 그 가변 부분은 여전히 변한다.
trap = ([1, 2], [3, 4])
trap[0].append(99)
assert trap == ([1, 2, 99], [3, 4])  # 튜플 자체는 그대로지만 내부 리스트는 변형됨

# ──── 7. 불변성 유지 패턴 — 새 객체 반환 ────

# (a) 변경 대신 새 객체를 반환하는 함수형 스타일
def push(stack: tuple, x: int) -> tuple:
    """기존 stack 을 건드리지 않고 새 튜플을 돌려준다."""
    return stack + (x,)

s = (1, 2, 3)
s2 = push(s, 4)
assert s == (1, 2, 3)
assert s2 == (1, 2, 3, 4)

# (b) frozen=True dataclass — 필드 재대입 자체를 금지
@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def translate(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)   # 새 인스턴스 반환

p = Point(1, 2)
p2 = p.translate(10, 20)
assert p == Point(1, 2)
assert p2 == Point(11, 22)

# ──── 8. MappingProxyType — dict 의 읽기 전용 뷰 ────

_internal = {"version": "1.0", "debug": False}
PUBLIC = MappingProxyType(_internal)   # 외부 노출용 읽기 전용 래퍼

assert PUBLIC["version"] == "1.0"
try:
    PUBLIC["debug"] = True             # 실패해야 정상
except TypeError as e:
    assert "does not support item assignment" in str(e)

# 주의: 원본 _internal 이 변하면 PUBLIC 으로 보는 값도 변한다 — "뷰"이지 "복사"가 아니다.
_internal["debug"] = True
assert PUBLIC["debug"] is True


# ──── 9. 다른 언어와의 비교 — Dart / TypeScript ────
#
# (1) 매핑 요약표
#
# 작업                         | Python                                | Dart                                      | TypeScript / JavaScript
# ---------------------------- | ------------------------------------- | ----------------------------------------- | --------------------------------------------
# 리스트 얕은 복사             | `a.copy()`, `list(a)`, `a[:]`,        | `List.from(a)`, `List.of(a)`,             | `[...a]`, `Array.from(a)`,
#                              | `copy.copy(a)`                        | `[...a]`                                  | `a.slice()`
# dict / Map 얕은 복사         | `d.copy()`, `dict(d)`, `{**d}`        | `Map.from(m)`, `{...m}`                   | `{...obj}`, `Object.assign({}, obj)`
# 깊은 복사                    | `copy.deepcopy(x)`                    | 직접 재귀 / `jsonDecode(jsonEncode(x))`   | `structuredClone(x)`  ← 모던 표준
#                              |                                       | / `package:freezed` 의 `copyWith`         | `JSON.parse(JSON.stringify(x))`  ← 구식
# 변수 재대입 금지             | `Final[T]` 힌트 (관례)                | `final x = ...;`                          | `const x = ...;`
# 컴파일 타임 상수             | (없음)                                | `const x = ...;`                          | `as const`
# 객체 자체 동결(얕은)         | `MappingProxyType(d)`                 | `List.unmodifiable(a)`, `Map.unmodifiable`| `Object.freeze(obj)`
# 깊은 동결                    | (재귀로 직접)                         | `package:freezed`, `@immutable`           | `Object.freeze` 재귀 + Immer / Immutable.js
# 불변 값 클래스               | `@dataclass(frozen=True)`             | `@immutable class`, `freezed`             | `Readonly<T>`, class with `readonly`
# 변경 시 새 인스턴스 반환     | `dataclasses.replace(p, x=1)`         | `p.copyWith(x: 1)`                        | `{ ...p, x: 1 }`
#
# (2) 얕은 복사 함정 — 세 언어 공통
#
# Python:
#     nested = [[1, 2], [3, 4]]
#     shallow = nested.copy()
#     shallow[0].append(99)       # nested 까지 [[1, 2, 99], [3, 4]] 로 오염
#
# Dart:
#     var nested = [[1, 2], [3, 4]];
#     var shallow = [...nested];
#     shallow[0].add(99);          // nested[0] 도 [1, 2, 99] — 같은 inner list 를 공유
#
# TypeScript:
#     const nested = [[1, 2], [3, 4]];
#     const shallow = [...nested];
#     shallow[0].push(99);         // nested[0] 도 [1, 2, 99]
#
# 어느 언어든 스프레드/얕은 복사는 **최상위 컨테이너만 새로** 만들고, 안의 객체는 공유한다.
#
# (3) 깊은 복사
#
# Python:        copy.deepcopy(nested)
# Dart:          // 표준 라이브러리에 한 줄짜리는 없음
#                // - JSON 직렬화 가능한 데이터면: jsonDecode(jsonEncode(nested))
#                // - 일반 객체면 직접 재귀 / freezed 의 copyWith 조합
# TypeScript:    structuredClone(nested)              // 함수·DOM 제외 거의 모든 값 OK
#                JSON.parse(JSON.stringify(nested))   // 함수·Date·Map·Set 손실, 구식
#
# (4) 불변 값 클래스 — "변경하려면 새 인스턴스" 패턴
#
# Python:
#     @dataclass(frozen=True)
#     class Point:
#         x: int
#         y: int
#     p2 = dataclasses.replace(p, x=10)
#
# Dart (freezed 패키지 관용구):
#     @freezed
#     class Point with _$Point {
#       const factory Point({required int x, required int y}) = _Point;
#     }
#     final p2 = p.copyWith(x: 10);
#
# TypeScript:
#     type Point = Readonly<{ x: number; y: number }>;
#     const p:  Point = { x: 1, y: 2 };
#     const p2: Point = { ...p, x: 10 };       // 스프레드 + 덮어쓰기
#
# 세 언어 모두 "원본은 그대로 두고, 변경된 새 객체를 돌려준다"는 동일한 함수형 스타일을 권장한다.
#
# (5) 핵심 정리
#
# - 어느 언어든 "복사를 명시적으로 요청하지 않으면 참조 공유"이고, 얕은 복사는 중첩 객체를 공유한다.
# - 깊은 복사는 비용이 크다 — 평탄 구조에는 쓰지 말고, 중첩 변형 격리가 필요할 때만 선택한다.
# - 변경 시 새 인스턴스를 만드는 패턴(파이썬 `dataclasses.replace`, Dart `copyWith`, TS 스프레드)이
#   현대 함수형 스타일의 사실상 표준이다.


if __name__ == "__main__":
    # 얕은 복사 함정 시연
    nested = [[1, 2], [3, 4]]
    shallow = nested.copy()
    shallow[0].append(99)
    print("얕은 복사 후 원본:", nested)        # [[1, 2, 99], [3, 4]] — 오염됨

    nested = [[1, 2], [3, 4]]
    deep = copy.deepcopy(nested)
    deep[0].append(99)
    print("깊은 복사 후 원본:", nested)        # [[1, 2], [3, 4]] — 보존

    # 불변 패턴
    p = Point(1, 2)
    p2 = p.translate(10, 20)
    print(f"원본 {p} → translate → 새 객체 {p2}")

    # 읽기 전용 뷰
    print("PUBLIC['version']:", PUBLIC["version"])
    try:
        PUBLIC["new"] = "x"
    except TypeError as e:
        print("쓰기 차단됨:", e)
