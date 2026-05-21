"""
연습문제 01 — 이터레이터 프로토콜
iter() 와 next() 를 직접 호출하고, StopIteration 을 잡아본다.
"""

# ──── TODO ────
# 1. iter([10, 20, 30]) 으로 이터레이터를 만든다.
# 2. next() 를 3번 호출해 각각 10, 20, 30 을 받는다.
# 3. 4번째 next() 호출 시 StopIteration 을 try/except 로 잡아
#    caught = True 로 설정한다.

it = iter([10, 20, 30])

a = None  # TODO: next(it)
b = None  # TODO: next(it)
c = None  # TODO: next(it)

caught = False
# TODO: try/except 로 StopIteration 을 잡아 caught = True 설정

# ──── 검증 (수정 금지) ────
assert a == 10,          f"a 는 10 이어야 합니다. 실제: {a}"
assert b == 20,          f"b 는 20 이어야 합니다. 실제: {b}"
assert c == 30,          f"c 는 30 이어야 합니다. 실제: {c}"
assert caught is True,   "StopIteration 을 잡지 못했습니다."
print("OK")
