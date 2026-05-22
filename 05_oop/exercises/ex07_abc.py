"""
연습문제 07: abc.ABC + Protocol.

3개 TODO 를 채워 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex07_abc.py`.
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ──── TODO 1: 추상 베이스 클래스 Animal ────
# speak() 를 추상 메서드로 강제하는 Animal 을 만드세요.

class Animal(ABC):
    # TODO: @abstractmethod 를 붙인 speak(self) -> str 선언
    pass


# 추상 메서드가 있으므로 직접 인스턴스화 시도는 TypeError 가 나야 한다.
try:
    Animal()
except TypeError:
    pass
else:
    raise AssertionError("Animal 이 여전히 인스턴스화됩니다 — @abstractmethod 누락?")


# ──── TODO 2: 구체 클래스 Dog ────
# Animal 을 상속해 speak() 를 "멍멍" 으로 구현하세요.

class Dog(Animal):
    # TODO
    pass


assert Dog().speak() == "멍멍"


# ──── TODO 3: Protocol — 상속 없이 호환 ────
# describe() 메서드가 있으면 만족하는 Describable Protocol 을 정의하세요.
# Protocol 은 `@runtime_checkable` 로 isinstance 검사가 가능하게 만드세요.

@runtime_checkable
class Describable(Protocol):
    # TODO: describe(self) -> str
    ...


class Book:
    """Describable 을 상속하지 않았지만 describe() 가 있으므로 호환되어야 한다."""
    def __init__(self, title: str):
        self.title = title

    def describe(self) -> str:
        return f"책: {self.title}"


b = Book("파이썬")
assert isinstance(b, Describable)
assert b.describe() == "책: 파이썬"


print("OK")
