"""
연습문제 02 — 숫자와 연산자

TODO 를 채워서 아래 조건을 만족시키세요:
  1. 2 의 10 제곱을 계산해 power 에 대입하세요.
  2. divmod(17, 5) 의 결과를 q, r 에 언패킹하세요.

모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

# TODO 1: 2 ** 10 을 계산해 power 에 대입하세요
power = ...

# TODO 2: divmod(17, 5) 결과를 q, r 에 언패킹하세요
q, r = ...

# ── 채점 (수정 금지) ──
assert power == 1024,  f"power 는 1024 이어야 합니다. 현재: {power!r}"
assert q == 3,         f"q(몫) 는 3 이어야 합니다. 현재: {q!r}"
assert r == 2,         f"r(나머지) 는 2 이어야 합니다. 현재: {r!r}"

print("OK")
