"""
연습문제 04 — 동적 클래스 생성
type() 을 사용해 클래스를 동적으로 만들고 인스턴스화하라.
"""

# ──── TODO ────
# type("Dynamic", (), {...}) 을 사용해
# greet 메서드를 가진 클래스 Dynamic 을 동적으로 생성하라.
# - greet(self) 는 문자열 "hi" 를 반환해야 한다.
# 그 후 인스턴스를 만들어 .greet() 를 호출하라.

# TODO: Dynamic 클래스를 type() 으로 생성하라
Dynamic = None   # 이 줄을 교체


# ──── 검증 ────

assert Dynamic is not None, "Dynamic 이 None — type() 으로 클래스를 생성하라"
assert Dynamic.__name__ == "Dynamic", f"클래스 이름이 'Dynamic' 이 아님: {Dynamic.__name__}"

obj = Dynamic()
assert hasattr(obj, "greet"), "Dynamic 인스턴스에 greet 메서드가 없음"
assert obj.greet() == "hi", f"greet() 가 'hi' 를 반환하지 않음: {obj.greet()!r}"

# 두 번째 인스턴스도 동일하게 동작해야 한다
obj2 = Dynamic()
assert obj2.greet() == "hi"

print("OK")
