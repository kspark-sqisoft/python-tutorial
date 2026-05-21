"""
정답 01 — 이터레이터 프로토콜

iter() 는 이터러블에서 이터레이터 객체를 만든다.
next() 는 이터레이터에서 값을 하나씩 꺼낸다.
더 꺼낼 값이 없으면 StopIteration 이 발생하므로
try/except 로 잡아 소진 여부를 확인할 수 있다.
"""

it = iter([10, 20, 30])

a = next(it)   # 10
b = next(it)   # 20
c = next(it)   # 30

caught = False
try:
    next(it)   # 이터레이터가 소진됐으므로 StopIteration 발생
except StopIteration:
    caught = True

# ──── 검증 (수정 금지) ────
assert a == 10,          f"a 는 10 이어야 합니다. 실제: {a}"
assert b == 20,          f"b 는 20 이어야 합니다. 실제: {b}"
assert c == 30,          f"c 는 30 이어야 합니다. 실제: {c}"
assert caught is True,   "StopIteration 을 잡지 못했습니다."
print("OK")
