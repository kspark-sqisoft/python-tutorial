"""
연습문제 04 — truthy / falsy

각 표현식의 bool() 결과를 예상해서 TODO 를 채우세요.

주의:
  - bool(0)    → False  (0 은 falsy)
  - bool("")   → False  (빈 문자열은 falsy)
  - bool("False") → ???  (문자열 "False" 는 비어있지 않다!)
  - bool([0])  → ???  (원소가 있는 리스트는 비어있지 않다!)

모든 assert 가 통과되면 "OK" 가 출력됩니다.
"""

# TODO 1: bool(0) 의 결과를 r1 에 대입하세요
r1 = ...

# TODO 2: bool("") 의 결과를 r2 에 대입하세요
r2 = ...

# TODO 3: bool("False") 의 결과를 r3 에 대입하세요
r3 = ...

# TODO 4: bool([0]) 의 결과를 r4 에 대입하세요
r4 = ...

# ── 채점 (수정 금지) ──
assert r1 == bool(0),       f"r1 오답. bool(0) = {bool(0)}"
assert r2 == bool(""),      f"r2 오답. bool('') = {bool('')}"
assert r3 == bool("False"), f"r3 오답. bool('False') = {bool('False')}"
assert r4 == bool([0]),     f"r4 오답. bool([0]) = {bool([0])}"

# 타입 검증
assert isinstance(r1, bool), "r1 은 bool 이어야 합니다."
assert isinstance(r2, bool), "r2 는 bool 이어야 합니다."
assert isinstance(r3, bool), "r3 는 bool 이어야 합니다."
assert isinstance(r4, bool), "r4 는 bool 이어야 합니다."

print("OK")
