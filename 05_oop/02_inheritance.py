"""
상속과 다형성 — 부모/자식 클래스, super(), 메서드 오버라이드,
isinstance/issubclass, 다형성(같은 메서드 이름 → 다른 동작).
"""

# ──── 1. 기본 상속 ────

# class 자식(부모): 형태로 상속한다.
class Animal:
    """모든 동물의 베이스 클래스."""

    def __init__(self, name):
        self.name = name  # 부모 클래스의 인스턴스 속성

    def sound(self):
        """동물 소리를 반환한다. 자식 클래스에서 오버라이드 예정."""
        return "...일반적인 동물 소리"

    def introduce(self):
        """이름과 소리를 함께 출력한다."""
        return f"저는 {self.name}, 제 소리는 '{self.sound()}' 입니다."


# ──── 2. 자식 클래스와 super() ────

# Dog 는 Animal 을 상속한다. super().__init__() 으로 부모 초기화를 위임한다.
class Dog(Animal):
    """개 클래스 — sound() 를 오버라이드한다."""

    def __init__(self, name, breed):
        super().__init__(name)  # 부모의 __init__ 호출: self.name 설정
        self.breed = breed      # 자식만의 추가 속성

    def sound(self):
        """메서드 오버라이드: 부모와 같은 이름, 다른 동작."""
        return "멍"


class Cat(Animal):
    """고양이 클래스 — sound() 를 오버라이드한다."""

    def sound(self):
        return "야옹"


# ──── 3. isinstance 와 issubclass ────

# isinstance(객체, 클래스): 객체가 해당 클래스(또는 그 자식)의 인스턴스인지 확인
# issubclass(자식, 부모): 클래스 계층 관계 확인
# 다중 상속은 가능하지만(MRO — Method Resolution Order 로 순서 결정) 여기서는 깊이 다루지 않는다.


# ──── 4. 다형성 ────

# 같은 메서드 이름(sound)이 클래스에 따라 다르게 동작한다.
# 리스트에 Animal, Dog, Cat 을 섞어 담아 동일하게 순회할 수 있다.


# ──── 5. 데모 ────

if __name__ == "__main__":
    animals = [
        Animal("동물"),
        Dog("바둑이", "진돗개"),
        Cat("나비"),
        Dog("초코", "말티즈"),
    ]

    print("=== 다형성 시연 ===")
    for a in animals:
        print(a.introduce())

    print()
    print("=== isinstance / issubclass ===")
    dog = animals[1]
    print(f"isinstance(dog, Dog)    → {isinstance(dog, Dog)}")     # True
    print(f"isinstance(dog, Animal) → {isinstance(dog, Animal)}")  # True (상속 관계)
    print(f"isinstance(dog, Cat)    → {isinstance(dog, Cat)}")     # False
    print(f"issubclass(Dog, Animal) → {issubclass(Dog, Animal)}")  # True
    print(f"issubclass(Cat, Dog)    → {issubclass(Cat, Dog)}")     # False
