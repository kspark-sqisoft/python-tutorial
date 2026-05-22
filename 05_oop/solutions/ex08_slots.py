"""
풀이 08: __slots__.

- `__slots__` 는 인스턴스가 가질 수 있는 속성 이름을 고정 슬롯으로 제한한다. 미선언 속성 추가는 AttributeError.
- `@dataclass(slots=True)` 는 dataclass 와 슬롯을 동시에 활용하는 가장 깔끔한 방법.
- 자식 클래스에서 `__slots__` 를 누락하면 `__dict__` 가 부활해 슬롯의 이점이 사라진다 — 자식에서도 명시해야 한다.
"""

from dataclasses import dataclass


class Coord:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


c = Coord(1, 2)
assert c.x == 1 and c.y == 2
try:
    c.z = 99
except AttributeError:
    pass
else:
    raise AssertionError
assert not hasattr(c, "__dict__")


@dataclass(slots=True)
class Item:
    name: str
    price: float


item = Item("사과", 1500.0)
assert item.name == "사과" and item.price == 1500.0
try:
    item.discount = 0.1
except AttributeError:
    pass
else:
    raise AssertionError


class Coord3D(Coord):
    __slots__ = ("z",)                          # 부모의 슬롯에 z 만 추가

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


c3 = Coord3D(1, 2, 3)
assert (c3.x, c3.y, c3.z) == (1, 2, 3)
assert not hasattr(c3, "__dict__")


print("OK")
