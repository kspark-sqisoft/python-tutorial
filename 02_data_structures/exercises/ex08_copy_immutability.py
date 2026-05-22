"""
연습문제 07: 얕은 복사 / 깊은 복사 / 불변 패턴.

다음 4개 TODO 를 채워서 모든 assert 를 통과하고 'OK' 가 출력되도록 만드세요.
힌트는 주석에. 정답은 `solutions/ex07_copy_immutability.py` 와 비교.
"""

import copy
from dataclasses import dataclass


# ──── TODO 1: 평탄 리스트의 얕은 복사 ────
# original 과 독립적인 새 리스트 flat_copy 를 만드세요.
# `.copy()`, `list(...)`, `[:]`, `copy.copy(...)` 중 무엇이든 됩니다.

original = [10, 20, 30]
flat_copy = None  # ← 여기 채우기

flat_copy.append(40)
assert original == [10, 20, 30], "원본이 변하면 안 됩니다"
assert flat_copy == [10, 20, 30, 40]


# ──── TODO 2: 중첩 리스트는 깊은 복사로 분리 ────
# nested 의 모든 중첩 레벨까지 완전히 분리된 사본 deep 을 만드세요.

nested = [[1, 2], [3, 4]]
deep = None  # ← 여기 채우기

deep[0].append(999)
assert nested == [[1, 2], [3, 4]], "원본이 오염되면 얕은 복사를 쓴 것입니다"
assert deep == [[1, 2, 999], [3, 4]]


# ──── TODO 3: 불변 패턴 — 기존 튜플은 그대로, 새 튜플을 돌려주는 push ────
# stack 끝에 x 를 추가한 새 튜플을 반환하세요.

def push(stack: tuple, x: int) -> tuple:
    # TODO: stack 을 변형하지 말고 새 튜플을 반환하세요.
    return None

s = (1, 2, 3)
s2 = push(s, 4)
assert s == (1, 2, 3), "원본 튜플은 그대로여야 합니다"
assert s2 == (1, 2, 3, 4)


# ──── TODO 4: frozen dataclass 로 불변 Point ────
# 필드 재대입이 차단되는 frozen Point 클래스를 완성하고,
# translate 가 새 Point 를 반환하도록 만드세요.

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def translate(self, dx: int, dy: int) -> "Point":
        # TODO: 새 Point 인스턴스를 반환하세요.
        return None


p = Point(1, 2)
p2 = p.translate(10, 20)
assert p == Point(1, 2), "원본 Point 가 변하면 안 됩니다"
assert p2 == Point(11, 22)

# frozen 이므로 필드 재대입은 FrozenInstanceError 가 나야 정상
try:
    p.x = 999
except Exception as e:
    assert type(e).__name__ == "FrozenInstanceError", f"예상치 못한 예외: {e!r}"
else:
    raise AssertionError("frozen=True 가 빠진 것 같습니다")


print("OK")
