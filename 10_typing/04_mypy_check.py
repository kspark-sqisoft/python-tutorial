"""
mypy 로 정적 타입 검증하기
mypy 는 Python 코드를 실행하지 않고도 타입 오류를 찾아주는 정적 검사기다.
이 파일 자체는 mypy 오류가 없어야 한다 — 의도된 타입 오류 예시는 주석 안에만 둔다.
"""

# ──── 1. mypy 실행 방법 ────

# 터미널에서 아래 명령으로 이 파일을 검사한다:
#   uv run mypy 10_typing/04_mypy_check.py
#
# 전체 폴더 검사:
#   uv run mypy 10_typing/
#
# 엄격 모드 (권장):
#   uv run mypy --strict 10_typing/

# ──── 2. 올바른 타입 힌트 예시 ────

def add(a: int, b: int) -> int:
    """두 정수를 더한다 — mypy 오류 없음."""
    return a + b


def greet(name: str) -> str:
    """이름으로 인사 문자열 반환 — mypy 오류 없음."""
    return f"안녕, {name}!"


def safe_sqrt(n: float) -> float | None:
    """양수면 제곱근, 음수면 None 반환."""
    if n < 0:
        return None
    return n ** 0.5


# ──── 3. 타입 에러 예시 — 주석 안에만 ────

# 아래 코드들은 mypy 가 오류를 보고한다. 실제로 실행하면 작동할 수도 있지만
# 타입 안전성이 깨진다.

# 예시 1: 잘못된 인자 타입
#   result = add("hello", "world")
#   # error: Argument 1 to "add" has incompatible type "str"; expected "int"

# 예시 2: 반환 타입 불일치
#   def bad_greet(name: str) -> int:
#       return name  # error: Incompatible return value type (got "str", expected "int")

# 예시 3: None 가능성 무시
#   val = safe_sqrt(-1)
#   print(val + 1)  # error: Item "None" of "float | None" has no attribute "__add__"

# 예시 4: 존재하지 않는 속성
#   x: int = 5
#   x.upper()  # error: "int" has no attribute "upper"

# ──── 4. type: ignore — 임시 무시 ────

# 특정 줄의 mypy 오류를 억제할 때 사용한다.
# 남발하면 타입 힌트의 이점이 사라지므로 최소화해야 한다.
#
# 예:
#   result = add("a", "b")  # type: ignore[arg-type]
#
# 에러 코드를 명시하는 것이 좋다:
#   # type: ignore[arg-type]    — 인자 타입 불일치 무시
#   # type: ignore[return-value] — 반환 타입 불일치 무시
#   # type: ignore[assignment]   — 변수 할당 타입 불일치 무시

# ──── 5. mypy 설정 (pyproject.toml) ────

# [tool.mypy]
# python_version = "3.12"
# strict = true          # 엄격 모드 — 권장
# ignore_missing_imports = true
#
# 엄격 모드가 활성화되면:
# - 모든 함수에 반환 타입 요구
# - Any 타입 사용 경고
# - 인자/반환 타입 누락 경고

if __name__ == "__main__":
    print("=== mypy 정적 검증 시연 ===")
    print(f"add(3, 4) = {add(3, 4)}")
    print(f"greet('mypy') = {greet('mypy')}")
    print(f"safe_sqrt(9.0) = {safe_sqrt(9.0)}")
    print(f"safe_sqrt(-1.0) = {safe_sqrt(-1.0)}")

    val = safe_sqrt(16.0)
    if val is not None:          # None 체크 후 사용 — mypy 도 만족
        print(f"safe_sqrt(16.0) + 1 = {val + 1}")

    print()
    print("이 파일을 mypy 로 검사하려면:")
    print("  uv run mypy 10_typing/04_mypy_check.py")
    print("전체 폴더 검사:")
    print("  uv run mypy 10_typing/")
