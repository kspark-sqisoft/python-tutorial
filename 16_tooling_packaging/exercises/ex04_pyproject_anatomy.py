"""
연습문제 04 — pyproject.toml 해부 (tomllib)
TODO: get_project_name 과 get_test_deps 함수를 완성하세요.
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
    # TODO: tomllib.loads() 로 파싱해 project.name 을 반환하세요.
    raise NotImplementedError


def get_test_deps(toml_str: str) -> list[str]:
    """TOML 문자열에서 [project.optional-dependencies] test 목록을 반환한다."""
    # TODO: tomllib.loads() 로 파싱해 test 의존성 목록을 반환하세요.
    raise NotImplementedError


if __name__ == "__main__":
    assert get_project_name(TOML_STR) == "myproj"
    assert get_test_deps(TOML_STR) == ["pytest"]
    print("OK")
