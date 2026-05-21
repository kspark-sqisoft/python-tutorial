"""
mypy — 정적 타입 검사기 재방문.
10_typing 에서 타입 힌트 문법을 다뤘고, 여기서는 mypy 도구 사용에 집중한다.
pyproject.toml 설정과 실제 타입 힌트 함수로 mypy 통과를 확인한다.
"""

# ──── 1. mypy 란? ────

# mypy 는 Python 코드의 타입 힌트를 정적으로 검사하는 도구다.
# 10_typing 에서 타입 힌트 문법을 배웠다 — 여기서는 도구 관점에 집중.

# ──── 2. 기본 명령 ────

COMMANDS: list[str] = [
    "uv run mypy 16_tooling_packaging/          # 폴더 전체 검사",
    "uv run mypy 16_tooling_packaging/03_mypy_recap.py  # 파일 단독 검사",
    "uv run mypy --strict .                     # 엄격 모드 (권장)",
    "uv run mypy --ignore-missing-imports .     # 서드파티 스텁 없어도 무시",
]

# ──── 3. pyproject.toml 설정 ────

PYPROJECT_EXAMPLE: str = """
[tool.mypy]
python_version = "3.12"
strict = true              # --strict 와 동일 (모든 검사 활성화)
ignore_missing_imports = true
"""

# ──── 4. mypy 가 잡는 오류 유형 ────

ERROR_EXAMPLES: dict[str, str] = {
    "arg-type": "인자 타입 불일치 (int 기대, str 전달)",
    "return-value": "반환 타입 불일치",
    "name-defined": "정의되지 않은 이름 참조",
    "no-untyped-def": "--strict 시 타입 힌트 없는 함수 오류",
}


# ──── 5. 타입 힌트 있는 함수 예시 (mypy 통과) ────


def greet(name: str, repeat: int = 1) -> str:
    """이름을 포함한 인사 문자열을 반환한다."""
    return (f"안녕하세요, {name}!" + " ") * repeat


def add(a: int, b: int) -> int:
    """두 정수를 더한다."""
    return a + b


def safe_divide(numerator: float, denominator: float) -> float | None:
    """0 나눗셈이면 None 을 반환한다."""
    if denominator == 0.0:
        return None
    return numerator / denominator


# ──── 6. Demo ────


def show_mypy_guide() -> None:
    """mypy 사용법을 출력한다."""
    print("=" * 60)
    print("  mypy — 정적 타입 검사기")
    print("=" * 60)

    print("\n[주요 명령]")
    for cmd in COMMANDS:
        print(f"  $ {cmd}")

    print("\n[pyproject.toml 설정 예시]")
    print(PYPROJECT_EXAMPLE)

    print("[mypy 가 잡는 오류 유형]")
    for code, desc in ERROR_EXAMPLES.items():
        print(f"  {code}: {desc}")

    print("\n[함수 실행 예시]")
    print(f"  greet('파이썬') = {greet('파이썬')!r}")
    print(f"  add(3, 4) = {add(3, 4)}")
    print(f"  safe_divide(10.0, 0.0) = {safe_divide(10.0, 0.0)}")
    print(f"  safe_divide(10.0, 3.0) = {safe_divide(10.0, 3.0):.4f}")


if __name__ == "__main__":
    show_mypy_guide()
