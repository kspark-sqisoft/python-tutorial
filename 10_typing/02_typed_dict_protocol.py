"""
TypedDict 와 Protocol — 구조 기반 타입 힌트
TypedDict: 딕셔너리 키/값에 정적 타입을 부여한다.
Protocol: 명시적 상속 없이 메서드 구조만으로 타입 호환성을 정의한다 (구조적 부분 타입).
"""

from typing import TypedDict, Protocol

# ──── 1. TypedDict ────

class UserDict(TypedDict):
    """사용자 딕셔너리 — 키와 값의 타입을 정적으로 정의."""
    name: str
    age: int


class ProductDict(TypedDict):
    """상품 딕셔너리."""
    title: str
    price: float
    in_stock: bool


def greet_user(user: UserDict) -> str:
    """TypedDict 를 인자로 받아 인사 문자열 반환."""
    return f"{user['name']}({user['age']}세)님 환영합니다!"


def discount_price(product: ProductDict, rate: float) -> float:
    """할인율을 적용한 가격 반환 (0.0 ~ 1.0)."""
    return product["price"] * (1 - rate)


# ──── 2. Protocol — 구조적 부분 타입 ────

class HasArea(Protocol):
    """넓이를 계산할 수 있는 객체 — area() 메서드만 있으면 만족."""
    def area(self) -> float: ...


class HasDescription(Protocol):
    """설명 문자열을 반환하는 객체."""
    def describe(self) -> str: ...


# Protocol 을 상속하지 않아도 메서드만 있으면 만족 (덕 타이핑 + 정적 검사)
class Circle:
    """원 — HasArea 를 명시하지 않았지만 area() 가 있으므로 호환."""
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def describe(self) -> str:
        return f"반지름 {self.radius}인 원"


class Square:
    """정사각형 — HasArea 를 명시하지 않았지만 area() 가 있으므로 호환."""
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def describe(self) -> str:
        return f"변의 길이 {self.side}인 정사각형"


def print_area(shape: HasArea) -> None:
    """HasArea Protocol 을 만족하는 어떤 객체든 받을 수 있다."""
    print(f"  넓이: {shape.area():.4f}")


def print_description(obj: HasDescription) -> None:
    """HasDescription Protocol 을 만족하는 어떤 객체든 받을 수 있다."""
    print(f"  설명: {obj.describe()}")


if __name__ == "__main__":
    # TypedDict 시연
    print("=== TypedDict ===")
    user: UserDict = {"name": "Alice", "age": 28}
    product: ProductDict = {"title": "파이썬 책", "price": 35000.0, "in_stock": True}

    print(greet_user(user))
    print(f"10% 할인 가격: {discount_price(product, 0.1):.0f}원")

    # Protocol 시연
    print("\n=== Protocol (구조적 부분 타입) ===")
    circle = Circle(5.0)
    square = Square(4.0)

    print("Circle:")
    print_area(circle)      # Circle 은 HasArea 를 상속하지 않았지만 호환
    print_description(circle)

    print("Square:")
    print_area(square)      # Square 도 마찬가지
    print_description(square)

    print("\n→ Protocol: 명시적 상속 없이 구조(메서드)만으로 호환성 판단")
    print("→ TypedDict: 평범한 dict 처럼 사용하되 키/값 타입은 정적 검증")
