"""
정답 04 — pyproject.toml 해부 (tomllib)
get_project_name 과 get_test_deps 함수 구현.
"""

import tomllib

TOML_STR: str = """
[project]
name = "myproj"
version = "1.0.0"

[project.optional-dependencies]
test = ["pytest"]
"""


def get_project_name(toml_str: str) -> str:
    """TOML 문자열에서 [project] name 값을 반환한다."""
    data = tomllib.loads(toml_str)
    return data["project"]["name"]


def get_test_deps(toml_str: str) -> list[str]:
    """TOML 문자열에서 [project.optional-dependencies] test 목록을 반환한다."""
    data = tomllib.loads(toml_str)
    return data["project"]["optional-dependencies"]["test"]


if __name__ == "__main__":
    assert get_project_name(TOML_STR) == "myproj"
    assert get_test_deps(TOML_STR) == ["pytest"]
    print("OK")
