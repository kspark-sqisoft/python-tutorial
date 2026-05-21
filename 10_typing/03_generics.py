"""
제네릭 (Generics) — PEP 695 신문법 (Python 3.12+)
타입 매개변수를 사용해 여러 타입에서 동작하는 재사용 가능한 함수/클래스를 작성한다.
Python 3.12 부터는 TypeVar 선언 없이 `def f[T](...)` 문법으로 간결하게 표현한다.
"""

# ──── 1. 옛 문법 (참고용) ────

# Python 3.11 이하에서는 TypeVar 로 타입 변수를 선언해야 했다.
# from typing import TypeVar
# T = TypeVar("T")
# def first_old(items: list[T]) -> T: ...

# Python 3.12 부터는 아래처럼 인라인으로 선언한다.

# ──── 2. 제네릭 함수 (PEP 695 신문법) ────

def first[T](items: list[T]) -> T:
    """리스트의 첫 번째 원소를 반환한다 — 어떤 타입이든 가능."""
    return items[0]


def last[T](items: list[T]) -> T | None:
    """리스트의 마지막 원소를 반환하고, 빈 리스트면 None."""
    return items[-1] if items else None


def zip_with_index[T](items: list[T]) -> list[tuple[int, T]]:
    """각 원소에 인덱스를 붙인 튜플 리스트를 반환한다."""
    return [(i, item) for i, item in enumerate(items)]


# ──── 3. 제네릭 클래스 (PEP 695 신문법) ────

class Stack[T]:
    """타입 안전한 LIFO 스택."""

    def __init__(self) -> None:
        self._items: list[T] = []   # 내부 저장소

    def push(self, x: T) -> None:
        """원소를 스택에 추가한다."""
        self._items.append(x)

    def pop(self) -> T | None:
        """스택 맨 위 원소를 꺼낸다. 비어 있으면 None."""
        return self._items.pop() if self._items else None

    def peek(self) -> T | None:
        """꺼내지 않고 맨 위 원소를 확인한다."""
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """스택이 비어 있으면 True."""
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


# ──── 4. bound — 타입 제한 ────

# 숫자 타입(int 또는 float)으로 T 를 제한한다.
def total[T: int | float](items: list[T]) -> T:
    """숫자 타입 리스트의 합을 반환한다."""
    result = items[0]
    for item in items[1:]:
        result = result + item  # type: ignore[operator,assignment]
    return result


if __name__ == "__main__":
    # 제네릭 함수 시연
    print("=== 제네릭 함수 ===")
    print(f"first([10, 20, 30]) = {first([10, 20, 30])}")
    print(f"first(['a', 'b', 'c']) = {first(['a', 'b', 'c'])}")
    print(f"last([1, 2, 3]) = {last([1, 2, 3])}")
    print(f"last([]) = {last([])}")
    print(f"zip_with_index(['x', 'y', 'z']) = {zip_with_index(['x', 'y', 'z'])}")

    # 제네릭 클래스 시연
    print("\n=== Stack[int] ===")
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    int_stack.push(3)
    print(f"push 3개: {int_stack}")
    print(f"peek: {int_stack.peek()}")
    print(f"pop: {int_stack.pop()}")
    print(f"pop 후: {int_stack}")

    print("\n=== Stack[str] ===")
    str_stack: Stack[str] = Stack()
    str_stack.push("파이썬")
    str_stack.push("제네릭")
    print(f"push 2개: {str_stack}")
    print(f"pop: {str_stack.pop()}")

    # bound 시연
    print("\n=== bound (T: int | float) ===")
    print(f"total([1, 2, 3]) = {total([1, 2, 3])}")
    print(f"total([1.5, 2.5]) = {total([1.5, 2.5])}")

    print("\n→ PEP 695 신문법: TypeVar 없이 def f[T](...), class C[T]: 로 제네릭 표현")
