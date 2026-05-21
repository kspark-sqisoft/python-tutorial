"""
연습문제 01 — 변수와 언패킹

TODO 를 채워서 아래 조건을 만족시키세요:
  1. age 에 정수 30 을 대입하세요.
  2. name 에 문자열 "Kee" 를 대입하세요.
  3. 튜플 언패킹으로 a = 1, b = 2 가 되게 하세요.

모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

# TODO 1: age 에 정수 30 을 대입하세요
age = ...

# TODO 2: name 에 문자열 "Kee" 를 대입하세요
name = ...

# TODO 3: 튜플 언패킹으로 a 와 b 를 동시에 대입하세요 (a=1, b=2)
a, b = ...

# ── 채점 (수정 금지) ──
assert age == 30,         f"age 는 30 이어야 합니다. 현재: {age!r}"
assert isinstance(age, int), "age 는 int 타입이어야 합니다."
assert name == "Kee",    f"name 은 'Kee' 이어야 합니다. 현재: {name!r}"
assert isinstance(name, str), "name 은 str 타입이어야 합니다."
assert a == 1,           f"a 는 1 이어야 합니다. 현재: {a!r}"
assert b == 2,           f"b 는 2 이어야 합니다. 현재: {b!r}"

print("OK")
