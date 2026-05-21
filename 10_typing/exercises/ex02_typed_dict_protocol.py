"""
연습문제 02 — TypedDict 와 Protocol
TODO: Book TypedDict 와 HasLength Protocol 을 정의하고 사용하라.
"""

from typing import TypedDict, Protocol

# ──── TODO 1 ────
# TypedDict 'Book' 을 정의하라.
# 필드: title (str), pages (int)

# class Book(TypedDict):
#     ...
raise NotImplementedError("TODO: Book TypedDict 를 정의하세요")


# ──── TODO 2 ────
# Protocol 'HasLength' 를 정의하라.
# 메서드: def __len__(self) -> int: ...

# class HasLength(Protocol):
#     ...


# ──── 검증 ────
book: Book = {"title": "파이썬 완전정복", "pages": 450}
assert book["title"] == "파이썬 완전정복"
assert book["pages"] == 450

# list 는 __len__ 을 가지므로 HasLength 를 자연스럽게 만족한다
items: list[int] = [1, 2, 3]
assert len(items) == 3

print("OK")
