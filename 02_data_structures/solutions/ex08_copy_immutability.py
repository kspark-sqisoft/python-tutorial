"""
풀이 07: 얕은 복사 / 깊은 복사 / 불변 패턴.

- 평탄 리스트는 `list.copy()` 같은 얕은 복사로 충분하다(원소가 불변이면 공유돼도 안전).
- 중첩 구조에서만 `copy.deepcopy()` 의 비용을 감수한다. 평탄 구조에 deepcopy 를 쓰는 건 낭비다.
- 불변을 강제하는 가장 깔끔한 두 가지 도구는 (1) 튜플처럼 처음부터 불변인 타입을 쓰는 것,
  (2) `@dataclass(frozen=True)` 로 필드 재대입을 막고 변경이 필요하면 새 인스턴스를 만드는 것이다.
"""

import copy
from dataclasses import dataclass


original = [10, 20, 30]
flat_copy = original.copy()                # list(original) / original[:] / copy.copy(original) 모두 동치

flat_copy.append(40)
assert original == [10, 20, 30]
assert flat_copy == [10, 20, 30, 40]


nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)               # 얕은 복사는 안쪽 리스트를 공유하므로 안 됨

deep[0].append(999)
assert nested == [[1, 2], [3, 4]]
assert deep == [[1, 2, 999], [3, 4]]


def push(stack: tuple, x: int) -> tuple:
    return stack + (x,)                    # 튜플 합치기 → 새 튜플 반환


s = (1, 2, 3)
s2 = push(s, 4)
assert s == (1, 2, 3)
assert s2 == (1, 2, 3, 4)


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def translate(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)


p = Point(1, 2)
p2 = p.translate(10, 20)
assert p == Point(1, 2)
assert p2 == Point(11, 22)

try:
    p.x = 999
except Exception as e:
    assert type(e).__name__ == "FrozenInstanceError"
else:
    raise AssertionError("frozen=True 가 작동하지 않습니다")


print("OK")
