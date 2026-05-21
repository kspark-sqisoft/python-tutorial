"""
풀이 03 — 매직 메서드

왜 이렇게 풀었나:
__eq__ 는 두 Vector 의 x, y 를 직접 비교한다. isinstance 검사로 다른 타입과의
비교 시 NotImplemented 를 반환해 Python 이 반대 방향 비교를 시도하도록 했다.
__add__ 는 기존 객체를 변경하지 않고 새 Vector 를 반환한다(불변 패턴).
__eq__ 를 정의하면 기본 __hash__ 가 None 이 되므로, set/dict 키로 쓰려면
__hash__ 도 같이 정의해야 한다는 점을 기억하자.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)
assert Vector(1, 2) == Vector(1, 2)
print("OK")
