"""
abc — 추상 베이스 클래스 (Abstract Base Class, PEP 3119).

다른 언어와의 차이점:
- Java/Dart/TypeScript 의 `abstract class` 와 거의 1:1 매핑.
- 추상 메서드를 구현하지 않은 채 인스턴스화하면 `TypeError` — 컴파일 타임은 아니지만 호출 시점에 차단된다.
- 파이썬에는 **두 가지** 인터페이스 도구가 있다:
  - `abc.ABC`     — 명시적 상속, "is-a" 관계. 코드가 클래스 트리에 묶인다 (런타임 강제).
  - `typing.Protocol` — 구조적 타이핑, "looks-like-a". 메서드 시그니처만 맞으면 호환 (정적 검사 위주).
- 새 코드에선 Protocol 이 더 유연하지만, 라이브러리 사용자에게 "반드시 이걸 구현해야 한다" 는 신호가
  필요할 땐 ABC 가 더 강하다. 자세한 비교는 파일 끝 섹션.
- `10_typing/02_typed_dict_protocol.py` 에 Protocol 단독 시연이 있다 — 여기선 둘의 차이에 초점.
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ──── 1. 기본 ABC ────

class Shape(ABC):
    """추상 도형. area() 와 perimeter() 구현을 자식 클래스에 강제한다."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    # 추상이 아닌 구체 메서드를 함께 가질 수 있다 — Java `abstract class` 와 동일.
    def describe(self) -> str:
        return f"area={self.area():.2f} perimeter={self.perimeter():.2f}"


# ──── 2. 인스턴스화 차단 ────

try:
    Shape()                                 # 추상 메서드가 있어 직접 생성 불가
except TypeError as e:
    # 메시지 예: "Can't instantiate abstract class Shape ..."
    assert "abstract" in str(e).lower()


# ──── 3. 구체 구현 ────

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h

    def perimeter(self) -> float:
        return 2 * (self.w + self.h)


rect = Rectangle(3, 4)
assert rect.area() == 12
assert rect.perimeter() == 14


# ──── 4. 부분 구현은 여전히 추상 ────

class IncompleteShape(Shape):
    def area(self) -> float:
        return 0.0
    # perimeter 미구현 → 인스턴스화 시점에 차단


try:
    IncompleteShape()
except TypeError:
    pass


# ──── 5. ABC vs Protocol — 같은 요구를 두 가지로 표현 ────

@runtime_checkable
class HasArea(Protocol):
    """area() 만 있으면 만족 — 상속 불필요."""
    def area(self) -> float: ...


class Circle:
    """Shape 를 **상속하지 않았지만** area() 가 있어 HasArea 와 호환된다."""
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r * self.r


def total_area(shapes: list[HasArea]) -> float:
    """HasArea 를 만족하는 어떤 객체든 합산 — 라이브러리 사용자의 자유도가 높다."""
    return sum(s.area() for s in shapes)


circ = Circle(5)
assert not isinstance(circ, Shape)          # Shape 트리에는 속하지 않는다
assert isinstance(circ, HasArea)            # 그러나 HasArea Protocol 은 만족 (runtime_checkable)
assert round(total_area([rect, circ]), 2) == round(12 + 3.14159 * 25, 2)


# ──── 6. 정리 ────
#
# 도구       | 결합도          | 검사 시점          | 추천 용도
# ABC        | 높음(상속 필요) | 인스턴스화 시점    | 도메인 핵심 계층, 런타임 강제가 필요한 경우
# Protocol   | 낮음(상속 불필요)| 정적(mypy) + opt. | 의존성 주입, 이미 존재하는 외부 타입까지 묶어 받기


# ──── 7. 다른 언어와의 비교 — Dart / TypeScript ────
#
# 작업                                   | Python                                  | Dart                                  | TypeScript
# -------------------------------------- | --------------------------------------- | ------------------------------------- | -----------------------------------
# 추상 클래스                            | `class C(ABC):` + `@abstractmethod`     | `abstract class C { ... }`            | `abstract class C { ... }`
# 추상 메서드                            | `@abstractmethod def m(self): ...`      | `void m();` (본문 없음)               | `abstract m(): void;`
# 인스턴스화 차단                        | 호출 시 `TypeError`                     | 컴파일 에러                           | 컴파일 에러
# 구조적 타이핑(인터페이스)              | `class P(Protocol): def m(self): ...`   | (Dart 는 모든 클래스가 암묵적 interface) | `interface P { m(): void }` 또는 `type P = { m(): void }`
# 런타임 인터페이스 검사                 | `@runtime_checkable` + `isinstance`     | `obj is P`                            | (런타임 검사 없음 — 타입 가드 직접)
#
# 핵심 차이
# - Dart 는 모든 클래스가 암묵적 interface 라 별도 `interface` 키워드가 없다 — 파이썬 Protocol 에 가까운 모델.
# - TS 는 컴파일러 검사 위주이고, 런타임 검사는 직접 타입 가드를 작성해야 한다.
# - 파이썬은 두 모델을 모두 제공하는 드문 언어 — 동적 + 명시적 강제 둘 다 가능.


if __name__ == "__main__":
    print(f"Rectangle: {rect.describe()}")
    print(f"Circle 은 Shape 트리에 속하지 않는다: isinstance(circ, Shape) = {isinstance(circ, Shape)}")
    print(f"Circle 은 HasArea Protocol 을 만족한다: isinstance(circ, HasArea) = {isinstance(circ, HasArea)}")
    print(f"총 면적: {total_area([rect, circ]):.2f}")
