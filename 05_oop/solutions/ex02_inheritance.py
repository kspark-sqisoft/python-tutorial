"""
풀이 02 — 상속과 다형성

왜 이렇게 풀었나:
Animal 에 공통 상태(name)와 기본 동작(sound)을 정의하고, Dog 는 sound 만 오버라이드한다.
Dog.__init__ 에서 super().__init__(name) 을 호출해 부모의 초기화 로직을 재사용했다.
이렇게 하면 부모에 새 속성이 추가되어도 자식은 super() 호출만으로 자동 반영된다.
다형성 덕분에 Animal 타입으로 선언된 변수에 Dog 인스턴스를 담아도 sound() 가 올바르게 동작한다.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "..."


class Dog(Animal):
    def sound(self):
        return "멍"


assert Dog("바둑이").sound() == "멍"
assert Animal("이름").sound() == "..."
print("OK")
