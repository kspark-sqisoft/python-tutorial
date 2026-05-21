"""
정답 04 — truthy / falsy

bool() 은 객체의 __bool__ 또는 __len__ 을 호출해 참/거짓을 결정한다.
0 과 빈 문자열은 falsy 이지만, 문자열 "False" 는 비어 있지 않으므로 truthy 다.
[0] 은 원소가 하나 있는 리스트이므로 truthy — 내용물이 0 이라도 관계없다.
이 네 가지 사례는 Python 초학자가 가장 자주 실수하는 truthy/falsy 패턴이다.
"""

r1 = False   # bool(0)       → False
r2 = False   # bool("")      → False
r3 = True    # bool("False") → True  (비어있지 않은 문자열)
r4 = True    # bool([0])     → True  (원소가 있는 리스트)

assert r1 == bool(0)
assert r2 == bool("")
assert r3 == bool("False")
assert r4 == bool([0])
assert isinstance(r1, bool)
assert isinstance(r2, bool)
assert isinstance(r3, bool)
assert isinstance(r4, bool)

print("OK")
