"""
풀이 07: ABC + Protocol.

- `abc.ABC` + `@abstractmethod` 는 "이 메서드는 자식이 반드시 구현하라" 는 강한 신호. 미구현 시 인스턴스화 시점에 TypeError.
- `typing.Protocol` 은 명시적 상속 없이 메서드 시그니처만 맞으면 호환 — 라이브러리 사용자의 자유도가 높다.
- `@runtime_checkable` 을 붙이면 `isinstance(obj, Proto)` 로 런타임 검사가 가능해진다 (메서드 존재만 검사).
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str: ...


try:
    Animal()
except TypeError:
    pass
else:
    raise AssertionError


class Dog(Animal):
    def speak(self) -> str:
        return "멍멍"


assert Dog().speak() == "멍멍"


@runtime_checkable
class Describable(Protocol):
    def describe(self) -> str: ...


class Book:
    def __init__(self, title: str):
        self.title = title

    def describe(self) -> str:
        return f"책: {self.title}"


b = Book("파이썬")
assert isinstance(b, Describable)
assert b.describe() == "책: 파이썬"


print("OK")
