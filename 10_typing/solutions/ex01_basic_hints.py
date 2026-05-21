"""
풀이 01 — 기본 타입 힌트
왜: str * n 은 파이썬의 문자열 반복 연산자다.
타입 힌트를 명시하면 mypy 가 s, n 의 타입을 정적으로 검증한다.
"""


def repeat(s: str, n: int) -> str:
    """s 를 n 번 반복한 문자열을 반환한다."""
    return s * n


assert repeat("ab", 3) == "ababab"
assert repeat("x", 1) == "x"
assert repeat("hi", 0) == ""
print("OK")
