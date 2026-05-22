"""
연습문제 08: __slots__.

3개 TODO 를 채워 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex08_slots.py`.
"""

from dataclasses import dataclass


# ──── TODO 1: __slots__ 를 가진 클래스 ────
# 좌표(x, y)만 허용하고 그 외 속성 추가는 차단되도록 Coord 클래스를 작성하세요.

class Coord:
    # TODO: __slots__ 를 ("x", "y") 로 선언하고 __init__ 작성
    pass


c = Coord(1, 2)
assert c.x == 1 and c.y == 2

# 슬롯에 없는 속성은 차단되어야 한다.
try:
    c.z = 99
except AttributeError:
    pass
else:
    raise AssertionError("__slots__ 가 제대로 동작하지 않습니다")

# 슬롯 클래스는 __dict__ 가 없다.
assert not hasattr(c, "__dict__")


# ──── TODO 2: @dataclass(slots=True) ────
# slots=True 옵션을 켠 dataclass Item 을 작성하세요. 필드: name(str), price(float).

@dataclass(slots=True)
class Item:
    # TODO
    pass


item = Item("사과", 1500.0)
assert item.name == "사과" and item.price == 1500.0

try:
    item.discount = 0.1
except AttributeError:
    pass
else:
    raise AssertionError("dataclass(slots=True) 가 제대로 동작하지 않습니다")


# ──── TODO 3: 자식 클래스에서 슬롯 유지 ────
# Coord 를 상속하고도 슬롯의 이점을 잃지 않도록, 자식에서도 __slots__ 를 빈 튜플로 선언하세요.

class Coord3D(Coord):
    # TODO: __slots__ = ("z",) 로 z 슬롯만 추가
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


c3 = Coord3D(1, 2, 3)
assert (c3.x, c3.y, c3.z) == (1, 2, 3)

# 자식도 슬롯만 가지므로 __dict__ 가 없어야 한다.
assert not hasattr(c3, "__dict__"), "자식에서 __slots__ 를 빠뜨리면 __dict__ 가 부활합니다"


print("OK")
