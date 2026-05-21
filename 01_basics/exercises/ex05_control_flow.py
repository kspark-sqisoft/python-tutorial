"""
연습문제 05 — 제어흐름 (for + if)

1 부터 20 까지의 정수 중 짝수만 모아 리스트 evens 를 만드세요.
for 루프와 if 조건문을 사용하세요.

모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

# TODO: for 루프와 if 를 사용해 1~20 중 짝수만 모은 리스트 evens 를 만드세요
evens = ...

# ── 채점 (수정 금지) ──
assert isinstance(evens, list),     f"evens 는 list 이어야 합니다. 현재: {type(evens).__name__}"
assert len(evens) == 10,            f"짝수는 10 개이어야 합니다. 현재: {len(evens) if isinstance(evens, list) else '?'}"
assert evens[0] == 2,               f"첫 번째 짝수는 2 이어야 합니다. 현재: {evens[0]!r}"
assert evens[-1] == 20,             f"마지막 짝수는 20 이어야 합니다. 현재: {evens[-1]!r}"
assert all(n % 2 == 0 for n in evens), "evens 의 모든 원소가 짝수이어야 합니다."

print("OK")
