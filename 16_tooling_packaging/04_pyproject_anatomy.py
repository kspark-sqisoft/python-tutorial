"""
pyproject.toml 해부 — 현대 Python 프로젝트의 중심 설정 파일.
tomllib (Python 3.11+ 표준 라이브러리) 로 실제 pyproject.toml 을 읽어
각 섹션의 역할을 확인한다.
"""

# ──── 1. pyproject.toml 섹션별 역할 ────

# [project]           : 패키지 메타데이터 (이름, 버전, requires-python, dependencies)
# [project.optional-dependencies] : 그룹별 선택 의존성 (dev, test, data 등)
# [build-system]      : 빌드 백엔드 지정 (hatchling, setuptools, flit 등)
# [tool.*]            : 도구별 설정 (ruff, black, mypy, pytest 등)

# ──── 2. tomllib 임포트 (3.11+ 표준 라이브러리) ────

import tomllib  # Python 3.11 부터 내장; 이전 버전은 tomli 패키지 필요
from pathlib import Path

# ──── 3. 섹션 설명 상수 ────

SECTION_ROLES: dict[str, str] = {
    "[project]": "패키지 이름, 버전, Python 버전 요건, 의존성",
    "[project.optional-dependencies]": "그룹별 추가 의존성 (pip install .[dev])",
    "[build-system]": "빌드 백엔드 및 빌드 도구 의존성",
    "[tool.ruff]": "ruff 린터 설정 (규칙 선택, 줄 길이 등)",
    "[tool.black]": "black 포매터 설정 (줄 길이, 대상 버전)",
    "[tool.mypy]": "mypy 타입 검사 설정 (strict 여부 등)",
    "[tool.pytest.ini_options]": "pytest 실행 옵션",
}


# ──── 4. pyproject.toml 읽기 함수 ────


def load_pyproject(path: Path) -> dict:  # type: ignore[type-arg]
    """주어진 경로의 pyproject.toml 을 파싱해 딕셔너리로 반환한다."""
    with path.open("rb") as f:  # tomllib 은 바이너리 모드 필요
        return tomllib.load(f)


def show_project_info(data: dict) -> None:  # type: ignore[type-arg]
    """[project] 섹션 핵심 정보를 출력한다."""
    project = data.get("project", {})
    print(f"  이름     : {project.get('name', '(없음)')}")
    print(f"  버전     : {project.get('version', '(없음)')}")
    print(f"  Python   : {project.get('requires-python', '(없음)')}")
    deps = project.get("dependencies", [])
    print(f"  의존성   : {deps if deps else '(없음)'}")


def show_optional_deps(data: dict) -> None:  # type: ignore[type-arg]
    """[project.optional-dependencies] 그룹 이름을 출력한다."""
    opt = data.get("project", {}).get("optional-dependencies", {})
    if opt:
        print(f"  그룹 목록: {list(opt.keys())}")
        for group, pkgs in opt.items():
            print(f"    [{group}]: {pkgs}")
    else:
        print("  (optional-dependencies 없음)")


# ──── 5. Demo ────


def main() -> None:
    """저장소 루트의 pyproject.toml 을 읽어 섹션 정보를 출력한다."""
    print("=" * 60)
    print("  pyproject.toml 해부")
    print("=" * 60)

    print("\n[섹션별 역할]")
    for section, role in SECTION_ROLES.items():
        print(f"  {section:<40} → {role}")

    # 저장소 루트 pyproject.toml 경로 (이 파일 기준 두 단계 위)
    repo_root = Path(__file__).parent.parent
    toml_path = repo_root / "pyproject.toml"

    print(f"\n[실제 파일 읽기: {toml_path}]")
    if not toml_path.exists():
        print("  pyproject.toml 파일을 찾을 수 없습니다.")
        return

    data = load_pyproject(toml_path)

    print("\n-- [project] --")
    show_project_info(data)

    print("\n-- [project.optional-dependencies] --")
    show_optional_deps(data)

    build = data.get("build-system", {})
    print("\n-- [build-system] --")
    print(f"  build-backend : {build.get('build-backend', '(없음)')}")
    print(f"  requires      : {build.get('requires', [])}")

    tool_keys = list(data.get("tool", {}).keys())
    print("\n-- [tool.*] 등록된 도구 --")
    print(f"  {tool_keys}")


if __name__ == "__main__":
    main()
