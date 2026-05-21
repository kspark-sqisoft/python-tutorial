"""
연습문제 01 — 기본 타입 힌트
TODO: repeat 함수를 완성하라.
"""

# ──── TODO ────
# def repeat(s: str, n: int) -> str: 함수를 작성하라.
# s 를 n 번 반복한 문자열을 반환한다.
# 예: repeat("ab", 3) → "ababab"

def repeat(s: str, n: int) -> str:
    raise NotImplementedError("TODO: 구현하세요")


# ──── 검증 ────
assert repeat("ab", 3) == "ababab"
assert repeat("x", 1) == "x"
assert repeat("hi", 0) == ""
print("OK")
