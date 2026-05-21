"""
black — 의견 강한(opinionated) Python 코드 포매터.
설정이 거의 없어 팀 전체가 동일한 스타일을 강제로 따르게 된다.
이 파일은 black 포매팅 기준을 충족하는 깨끗한 코드 예시다.
"""

# ──── 1. black 이란? ────

# black 은 "the uncompromising code formatter".
# PEP 8 을 기반으로 하지만 black 만의 세부 규칙이 있다.
# 쌍따옴표 강제, 트레일링 쉼표, 줄 길이 88자 기본.

# ──── 2. 기본 명령 ────

COMMANDS: list[str] = [
    "uv run black 16_tooling_packaging/          # 실제 포매팅 적용",
    "uv run black --check 16_tooling_packaging/  # 수정 없이 확인만",
    "uv run black --diff 16_tooling_packaging/   # 변경 예정 내용 미리보기",
    "uv run black --line-length 100 .            # 줄 길이 재정의",
]

# ──── 3. pyproject.toml 설정 ────

PYPROJECT_EXAMPLE: str = """
[tool.black]
line-length = 88          # 기본값 (변경 가능하지만 권장하지 않음)
target-version = ["py312"]
"""

# ──── 4. black 이 바꾸는 것들 ────

STYLE_RULES: dict[str, str] = {
    "따옴표": "단따옴표 → 쌍따옴표로 통일",
    "트레일링 쉼표": "여러 줄 컬렉션에 마지막 쉼표 추가",
    "괄호 줄바꿈": "긴 줄은 자동으로 여러 줄로 분리",
    "공백 정규화": "불필요한 공백 제거·정리",
}


# ──── 5. Demo ────


def show_black_guide() -> None:
    """black 사용법을 출력한다."""
    print("=" * 60)
    print("  black — 의견 강한 Python 코드 포매터")
    print("=" * 60)

    print("\n[주요 명령]")
    for cmd in COMMANDS:
        print(f"  $ {cmd}")

    print("\n[pyproject.toml 설정 예시]")
    print(PYPROJECT_EXAMPLE)

    print("[black 이 자동으로 처리하는 스타일]")
    for rule, desc in STYLE_RULES.items():
        print(f"  {rule}: {desc}")

    print("\n팁: --check 로 CI 에서 포매팅 위반을 감지할 수 있다.")
    print("이 파일은 black --check 를 통과합니다.")


if __name__ == "__main__":
    show_black_guide()
