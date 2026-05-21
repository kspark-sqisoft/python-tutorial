"""
연습문제 04 — mypy 로 정적 검증
아래 함수를 완성한 뒤 mypy 로 검사해 오류가 없는지 확인하라.

mypy 실행 방법:
  uv run mypy 10_typing/exercises/ex04_mypy_check.py

전체 exercises 폴더 검사:
  uv run mypy 10_typing/exercises/
"""

# ──── TODO ────
# double 함수를 완성하라.
# def double(x: int) -> int: 정수를 두 배로 반환한다.

def double(x: int) -> int:
    raise NotImplementedError("TODO: 구현하세요")


# ──── 검증 ────
assert double(5) == 10
assert double(0) == 0
assert double(-3) == -6
print("OK")
