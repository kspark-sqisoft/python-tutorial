"""
풀이 01 — 클래스 기본

왜 이렇게 풀었나:
Rectangle 은 너비와 높이라는 두 가지 상태를 가지고, 넓이와 둘레라는 두 가지 행동을
제공하는 전형적인 값 객체다. __init__ 에서 인스턴스 속성으로 저장하고, 각 메서드는
self.width / self.height 를 참조해 계산만 수행한다. 부수 효과 없이 값을 반환하므로
테스트가 단순하고 재사용하기 쉽다.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


assert Rectangle(3, 4).area() == 12
assert Rectangle(3, 4).perimeter() == 14
print("OK")
