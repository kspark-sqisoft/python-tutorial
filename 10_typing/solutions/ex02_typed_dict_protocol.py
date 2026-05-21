"""
풀이 02 — TypedDict 와 Protocol
왜: TypedDict 는 dict 를 그대로 사용하되 키/값 타입을 정적으로 명세한다.
Protocol 은 명시적 상속 없이 메서드 구조만으로 호환성을 정의하는 구조적 부분 타입이다.
list 는 이미 __len__ 을 구현하므로 HasLength Protocol 을 자동으로 만족한다.
"""

from typing import TypedDict, Protocol


class Book(TypedDict):
    """도서 정보 TypedDict."""
    title: str
    pages: int


class HasLength(Protocol):
    """__len__ 메서드를 가진 객체를 표현하는 Protocol."""
    def __len__(self) -> int: ...


book: Book = {"title": "파이썬 완전정복", "pages": 450}
assert book["title"] == "파이썬 완전정복"
assert book["pages"] == 450

items: list[int] = [1, 2, 3]
assert len(items) == 3
print("OK")
