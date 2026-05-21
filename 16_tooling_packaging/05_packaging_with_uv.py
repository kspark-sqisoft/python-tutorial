"""
uv 패키징 흐름 — 빌드부터 PyPI 배포까지 명령 안내.
실제 build/publish 는 학습자가 수동으로 수행하며,
이 파일은 각 단계와 파일 형식을 설명한다.
"""

# ──── 1. 배포 파일 형식 ────

# .whl  (wheel)  : 바이너리 배포 포맷. 압축 아카이브로 설치 속도가 빠르다.
# .tar.gz (sdist): 소스 배포 포맷. 빌드 환경 없이도 소스 공유 가능.

# ──── 2. SemVer (유의적 버전) ────

# MAJOR.MINOR.PATCH  예: 1.2.3
# MAJOR: 하위 호환 불가 변경
# MINOR: 하위 호환 새 기능 추가
# PATCH: 버그 수정
SEMVER_EXAMPLE: str = "1.2.3"

# ──── 3. 빌드 및 배포 명령 ────

STEPS: list[tuple[str, str, str]] = [
    # (단계, 명령, 설명)
    ("1. 버전 확인", "pyproject.toml 에서 version 필드 수정", "SemVer 규칙 준수"),
    ("2. 빌드", "uv build", "dist/*.whl 과 dist/*.tar.gz 생성"),
    ("3. 확인", "uv run twine check dist/*", "배포 전 메타데이터 검증 (선택)"),
    (
        "4. TestPyPI",
        "uv publish --publish-url https://test.pypi.org/legacy/",
        "실제 배포 전 테스트",
    ),
    ("5. PyPI 배포", "uv publish", "PyPI 에 정식 업로드"),
    ("6. 설치 확인", "uv pip install <패키지이름>", "배포 후 정상 설치 확인"),
]

# ──── 4. wheel 파일 이름 구조 ────

# {name}-{version}-{python}-{abi}-{platform}.whl
# 예: myproj-1.0.0-py3-none-any.whl
#   name     = myproj
#   version  = 1.0.0
#   python   = py3  (CPython 3.x)
#   abi      = none (순수 Python)
#   platform = any  (플랫폼 무관)

WHEEL_EXAMPLE: str = "myproj-1.0.0-py3-none-any.whl"


# ──── 5. Demo ────


def show_packaging_guide() -> None:
    """uv 패키징 단계를 표 형식으로 출력한다."""
    print("=" * 65)
    print("  uv 패키징 흐름 — 빌드 → 검증 → 배포")
    print("=" * 65)

    print(f"\n[SemVer 예시: {SEMVER_EXAMPLE}]")
    print("  MAJOR.MINOR.PATCH → 1=주요변경, 2=기능추가, 3=버그수정")

    print("\n[배포 단계]")
    print(f"  {'단계':<20} {'명령/내용':<50} {'비고'}")
    print("  " + "-" * 80)
    for step, cmd, note in STEPS:
        print(f"  {step:<20} {cmd:<50} {note}")

    print(f"\n[wheel 파일 이름 예시: {WHEEL_EXAMPLE}]")
    parts = WHEEL_EXAMPLE.replace(".whl", "").split("-")
    labels = ["name", "version", "python", "abi", "platform"]
    for label, part in zip(labels, parts):
        print(f"  {label:<10} = {part}")

    print("\n빌드 결과물은 dist/ 폴더에 생성됩니다.")
    print("  $ uv build")
    print("  dist/myproj-1.0.0-py3-none-any.whl")
    print("  dist/myproj-1.0.0.tar.gz")


if __name__ == "__main__":
    show_packaging_guide()
