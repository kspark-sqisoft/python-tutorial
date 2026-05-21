"""
풀이 04 — mypy 로 정적 검증
왜: 타입 힌트를 명시한 간단한 함수도 mypy 로 검증해 타입 안전성을 확인할 수 있다.
    x * 2 는 int 를 반환하므로 -> int 반환 타입과 일치한다.

mypy 실행 방법:
  uv run mypy 10_typing/solutions/ex04_mypy_check.py
"""


def double(x: int) -> int:
    """정수를 두 배로 반환한다."""
    return x * 2


assert double(5) == 10
assert double(0) == 0
assert double(-3) == -6
print("OK")
