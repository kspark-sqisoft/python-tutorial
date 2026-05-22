"""
__slots__ — 인스턴스 속성을 고정 슬롯에 저장 (메모리 절약 + 오타 방지).

다른 언어와의 차이점:
- 파이썬 인스턴스는 기본적으로 `__dict__` 를 갖고 있어 **선언하지 않은 속성도 동적으로 추가**할 수 있다.
  Java/Dart/TypeScript 처럼 "선언된 필드만" 갖게 하려면 명시적으로 `__slots__` 를 정의해야 한다.
- 효과:
  (1) 선언 외 속성 추가 시 AttributeError — 오타로 인한 silent bug 방지
  (2) dict 오버헤드가 사라져 메모리 사용량 감소 (대량 인스턴스에서 수십 % 단위)
- 트레이드오프: 다중 상속/믹스인이 까다로워지고, weakref 가 필요하면 `'__weakref__'` 슬롯을 추가해야 한다.
- `@dataclass(slots=True)` 로 dataclass 와 결합하면 가장 깔끔하다.
- 자세한 언어 비교는 파일 끝 섹션.
"""

import sys
from dataclasses import dataclass


# ──── 1. 기본 클래스 — 임의 속성 추가 가능 (놀라운 부분) ────

class PointDict:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


p = PointDict(1, 2)
p.z = 99                                    # 선언하지 않았는데도 그냥 추가됨
assert p.z == 99
assert p.__dict__ == {"x": 1, "y": 2, "z": 99}
# → Java/Dart 출신이 가장 놀라는 부분. 오타(`p.X` 대신 `p.x` 를 의도)도 silent 하게 통과한다.


# ──── 2. __slots__ 사용 — 슬롯만 허용 ────

class PointSlot:
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


s = PointSlot(1, 2)
try:
    s.z = 99                                # 슬롯에 없는 속성 → AttributeError
except AttributeError:
    pass
assert not hasattr(s, "__dict__")           # 슬롯 클래스는 __dict__ 자체가 없다


# ──── 3. 메모리 비교 ────

dict_total = sys.getsizeof(p) + sys.getsizeof(p.__dict__)
slot_total = sys.getsizeof(s)
# slot_total 이 일반적으로 30~50% 작다 (구현·플랫폼마다 다름).
# 인스턴스를 수십만~수백만 개 만드는 시뮬레이션·ETL 코드에서 체감이 크다.


# ──── 4. @dataclass(slots=True) — 가장 권장되는 결합 ────

@dataclass(slots=True)
class Vec3:
    x: float
    y: float
    z: float


v = Vec3(1.0, 2.0, 3.0)
try:
    v.w = 4.0                               # 슬롯에 없는 속성 추가 → AttributeError
except AttributeError:
    pass

# 변경 자체를 막고 싶다면 `@dataclass(slots=True, frozen=True)` 처럼 둘을 결합하기도 한다.
# 단, 일부 환경에서 두 옵션이 만들어내는 __setattr__ 의 super() 처리가 미묘해
# 학습 시연에서는 분리해서 보여주는 편이 안전하다.
# 불변 dataclass 자체는 02_data_structures/08_copy_immutability.py 의 frozen Point 예시에서 다뤘다.


# ──── 5. 자주 만나는 함정 ────

# (a) 자식 클래스가 __slots__ 를 빼면 다시 __dict__ 가 생긴다 — 슬롯의 이점이 사라진다.
class P2(PointSlot):
    pass                                    # __slots__ 미선언 → __dict__ 부활


p2 = P2(1, 2)
p2.z = 99                                   # 다시 동작함
assert hasattr(p2, "__dict__")

# 해결: 자식에서도 명시적으로 `__slots__ = ()` 를 빈 튜플로라도 적어준다.
class P3(PointSlot):
    __slots__ = ()


p3 = P3(1, 2)
try:
    p3.z = 99
except AttributeError:
    pass


# (b) weakref 가 필요한 경우 슬롯에 '__weakref__' 를 명시해야 한다.
class Ref:
    __slots__ = ("data", "__weakref__")


# (c) 클래스 변수 기본값을 슬롯 이름과 같이 두면 충돌한다 — 슬롯은 디스크립터로 구현되기 때문.
# class Bad:
#     __slots__ = ("x",)
#     x = 0                                 # ValueError 발생


# ──── 6. 언제 쓸 것인가 ────
#
# - 대량 인스턴스 (10k+) 의 메모리가 부담스러울 때.
# - 도메인 객체가 "이 필드들만" 갖길 강제하고 싶을 때(오타·계약 위반 차단).
# - 단발성 스크립트나 일반 비즈니스 객체는 굳이 안 써도 된다 — `@dataclass` 만으로 충분.


# ──── 7. 다른 언어와의 비교 — Dart / TypeScript ────
#
# 작업                              | Python                              | Dart                                  | TypeScript
# --------------------------------- | ----------------------------------- | ------------------------------------- | --------------------------------------
# 필드 선언 강제                    | `__slots__ = ("x", "y")`            | 클래스 본문의 필드 선언 (기본값)      | `class { x: number; y: number; }`
# 미선언 속성 차단                  | 자동 (slots 사용 시)                | 자동 (컴파일 에러)                    | `--strict` + `noImplicitAny` 일 때 자동
# 인스턴스 생성 후 필드 추가 차단   | slots 또는 frozen dc                | 기본 동작                             | 기본 동작
# 메모리 최적화                     | slots → dict 제거                   | 컴파일러가 처리                       | 런타임 객체는 V8 hidden class 로 최적화
# frozen + slots                    | `@dataclass(slots=True, frozen=True)`| `@immutable` + `final` 필드           | `Readonly<{ ... }>` 또는 `class { readonly ... }`
#
# 핵심 차이
# - Java/Dart/TS 는 필드 선언이 **기본 강제** — 파이썬만 "기본은 동적, 원하면 강제"의 옵트인 모델이다.
# - 그래서 다른 언어 출신이 처음 파이썬을 만나면 "왜 임의 속성이 통과하지?" 라는 의문이 생긴다.
#   `__slots__` 가 그 의문에 대한 파이썬 측의 공식 답.


if __name__ == "__main__":
    print(f"PointDict 인스턴스 dict: {p.__dict__}")
    print(f"PointDict 메모리: {dict_total} bytes")
    print(f"PointSlot 메모리: {slot_total} bytes (작을수록 좋음)")
    print(f"Vec3 (slots+frozen): {v}")
    print(f"P2(상속 시 슬롯 깨짐) has __dict__: {hasattr(p2, '__dict__')}")
    print(f"P3(자식도 __slots__=()) has __dict__: {hasattr(p3, '__dict__')}")
