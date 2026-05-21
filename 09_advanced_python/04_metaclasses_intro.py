"""
메타클래스(Metaclass) 맛보기 모듈.
type() 의 두 가지 용법, 동적 클래스 생성,
그리고 __init_subclass__ 대안까지 간단히 살펴본다.
"""

# ──── 1. type() 의 두 가지 얼굴 ────

# type(obj)         → obj 의 클래스를 반환
# type(클래스)      → 클래스의 메타클래스를 반환 (대부분 type 자체)

class Dog:
    pass

fido = Dog()

# type(fido) 는 Dog, type(Dog) 는 type
# 즉 "클래스를 만드는 클래스"가 메타클래스이고 기본값이 type 이다


# ──── 2. 모든 클래스의 기본 메타클래스는 type ────

# class Foo:          →  내부적으로  Foo = type("Foo", (object,), {})
# class Bar(Foo):     →  Bar = type("Bar", (Foo,), {})
#
# 메타클래스를 직접 지정하려면:
#   class MyClass(metaclass=MyMeta): ...
# 하지만 일반 학습자가 직접 만들 일은 거의 없다


# ──── 3. type 으로 클래스 동적 생성 ────

# type(이름, 베이스 튜플, 속성 딕트)  →  새 클래스

# 인사 메서드를 가진 클래스를 동적으로 생성
Greeter = type(
    "Greeter",                              # 클래스 이름
    (),                                     # 베이스 클래스 없음 (object 상속)
    {"greet": lambda self: "안녕하세요!"},  # 속성/메서드 딕트
)

# 수학 유틸리티 클래스를 동적으로 생성
MathUtil = type(
    "MathUtil",
    (),
    {
        "square": lambda self, n: n * n,    # 제곱
        "cube":   lambda self, n: n * n * n, # 세제곱
    },
)


# ──── 4. __init_subclass__ — 메타클래스 대안 ────

# 메타클래스 없이 서브클래스 생성을 가로채는 더 간단한 방법
# 라이브러리 제작자가 서브클래스에 규칙을 강제할 때 유용하다

class PluginBase:
    """등록된 플러그인을 자동으로 추적하는 베이스 클래스."""
    _registry = []   # 등록된 서브클래스 목록

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase._registry.append(cls)   # 서브클래스 정의 시 자동 등록
        print(f"[PluginBase] {cls.__name__} 등록됨")


class PluginA(PluginBase):
    pass


class PluginB(PluginBase):
    pass


# ──── 5. 메타클래스 직접 작성 예 (참고용) ────

# 실제 메타클래스는 type 을 상속하고 __new__ 또는 __init__ 을 오버라이드한다
# 아래는 클래스 이름을 대문자로 강제하는 간단한 예시 (실무에서는 드물게 사용)

class UpperNameMeta(type):
    """클래스 이름을 자동으로 대문자로 변환하는 메타클래스."""
    def __new__(mcs, name, bases, namespace):
        return super().__new__(mcs, name.upper(), bases, namespace)


class hello(metaclass=UpperNameMeta):   # 소문자로 정의해도
    pass                                # 실제 이름은 대문자가 된다


if __name__ == "__main__":
    # type() 기초 확인
    print("=== type() 확인 ===")
    print(f"type(fido)  = {type(fido)}")    # <class '__main__.Dog'>
    print(f"type(Dog)   = {type(Dog)}")     # <class 'type'>
    print(f"type(type)  = {type(type)}")    # <class 'type'> — type 은 자기 자신의 메타클래스

    print()

    # 동적 클래스 생성 시연
    print("=== 동적 클래스 생성 ===")
    g = Greeter()
    print(f"Greeter 인스턴스: {g.greet()}")

    m = MathUtil()
    print(f"MathUtil.square(5) = {m.square(5)}")
    print(f"MathUtil.cube(3)   = {m.cube(3)}")

    print()

    # __init_subclass__ 시연
    print("=== __init_subclass__ ===")
    print(f"등록된 플러그인: {[cls.__name__ for cls in PluginBase._registry]}")

    print()

    # 메타클래스 이름 변환 확인
    print("=== UpperNameMeta ===")
    print(f"hello.__name__ = {hello.__name__}")   # HELLO
