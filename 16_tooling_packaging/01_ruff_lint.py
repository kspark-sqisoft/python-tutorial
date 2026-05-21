"""
ruff — Rust 로 만든 빠른 Python 린터.
flake8, isort, pylint 의 주요 규칙을 하나로 대체한다.
이 파일 자체는 ruff 검사를 통과하는 깨끗한 코드 예시다.
"""

# ──── 1. ruff 란? ────

# ruff 는 Rust 로 구현되어 flake8 보다 10~100배 빠르다.
# PEP 8 스타일, import 정렬, 미사용 변수 등 수백 가지 규칙 지원.

# ──── 2. 기본 명령 ────

COMMANDS: list[str] = [
    "uv run ruff check 16_tooling_packaging/          # 린트 검사",
    "uv run ruff check --fix 16_tooling_packaging/    # 자동 수정",
    "uv run ruff check --select ALL .                 # 모든 규칙 활성화",
    "uv run ruff format .                             # ruff 포매터 (black 호환)",
]

# ──── 3. pyproject.toml 설정 ────

PYPROJECT_EXAMPLE: str = """
[tool.ruff]
line-length = 100          # 최대 줄 길이
target-version = "py312"   # 대상 Python 버전

[tool.ruff.lint]
select = ["E", "F", "I"]   # E=pycodestyle, F=pyflakes, I=isort
ignore = ["E501"]          # 특정 규칙 제외
"""

# ──── 4. 자주 잡히는 문제 유형 ────

RULE_EXAMPLES: dict[str, str] = {
    "F401": "import os  # 사용하지 않는 임포트",
    "E711": "if x == None  # None 비교는 'is None' 권장",
    "I001": "import 순서 불일치 (isort 규칙)",
    "F841": "x = 1  # 대입 후 사용 안 함",
}


# ──── 5. Demo ────


def show_ruff_guide() -> None:
    """ruff 사용법을 출력한다."""
    print("=" * 60)
    print("  ruff — Rust 기반 빠른 Python 린터")
    print("=" * 60)

    print("\n[주요 명령]")
    for cmd in COMMANDS:
        print(f"  $ {cmd}")

    print("\n[pyproject.toml 설정 예시]")
    print(PYPROJECT_EXAMPLE)

    print("[자주 잡히는 규칙]")
    for code, desc in RULE_EXAMPLES.items():
        print(f"  {code}: {desc}")

    print("\n이 파일 자체는 ruff 가 통과합니다.")
    print("  $ uv run ruff check 16_tooling_packaging/01_ruff_lint.py")


if __name__ == "__main__":
    show_ruff_guide()
