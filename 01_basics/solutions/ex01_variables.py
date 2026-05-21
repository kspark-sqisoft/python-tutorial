"""
정답 01 — 변수와 언패킹

age 와 name 은 각각 리터럴 값을 직접 대입한다.
튜플 언패킹은 오른쪽의 (1, 2) 튜플을 왼쪽 두 이름에 동시에 묶는다.
Python 의 다중 대입은 임시 변수 없이 두 값을 교환할 때도 활용된다.
"""

age = 30
name = "Kee"
a, b = 1, 2

assert age == 30
assert isinstance(age, int)
assert name == "Kee"
assert isinstance(name, str)
assert a == 1
assert b == 2

print("OK")
