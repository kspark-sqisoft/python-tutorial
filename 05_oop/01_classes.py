"""
클래스 기본 — 클래스 선언, 인스턴스 속성, 클래스 속성, self 의 의미.
Point 클래스로 두 점 사이 거리를 계산하고,
Counter 클래스로 클래스 속성(공유 상태)을 실습한다.
"""

import math

# ──── 1. 클래스 선언과 self ────

# class 키워드로 새 타입을 정의한다.
# self 는 자바의 this 와 비슷하지만, Python 에서는 첫 번째 인자로 명시적으로 써야 한다.
# __init__ 은 초기화자: 객체는 __new__ 가 먼저 만들고, __init__ 은 그 객체를 초기화한다.
class Point:
    """2차원 좌표를 나타내는 클래스."""

    def __init__(self, x, y):
        # 인스턴스 속성: self.x, self.y 는 이 객체만의 데이터
        self.x = x
        self.y = y

    def distance_to(self, other):
        """다른 Point 까지의 유클리드 거리를 반환한다."""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


# ──── 2. 클래스 속성 vs 인스턴스 속성 ────

# 클래스 속성은 클래스 자체에 붙어 있어 모든 인스턴스가 공유한다.
# 인스턴스 속성은 각 객체마다 따로 존재한다.
class Counter:
    """생성된 횟수를 클래스 속성으로 추적하는 카운터."""

    total = 0  # 클래스 속성: 모든 Counter 인스턴스가 공유

    def __init__(self, label):
        self.label = label          # 인스턴스 속성: 이 객체만의 레이블
        Counter.total += 1          # 클래스 이름으로 접근해 공유 카운터 증가


# ──── 3. 데모 ────

if __name__ == "__main__":
    # Point 거리 계산
    p1 = Point(3, 4)
    p2 = Point(0, 0)
    dist = p1.distance_to(p2)
    print(f"Point({p1.x}, {p1.y}) 에서 Point({p2.x}, {p2.y}) 까지 거리: {dist}")  # 5.0

    # 클래스 속성으로 인스턴스 수 추적
    c1 = Counter("첫 번째")
    c2 = Counter("두 번째")
    c3 = Counter("세 번째")
    print(f"Counter 생성 횟수: {Counter.total}")  # 3

    # 인스턴스 속성은 객체마다 다름
    print(f"c1.label = {c1.label}, c2.label = {c2.label}")
