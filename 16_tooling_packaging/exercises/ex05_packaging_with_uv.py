"""
연습문제 05 — wheel 파일 이름 파싱
TODO: parse_wheel_filename 함수를 완성하세요.
wheel 파일 이름 형식: {name}-{version}-{python}-{abi}-{platform}.whl
"""


def parse_wheel_filename(filename: str) -> dict[str, str]:
    """wheel 파일 이름에서 name 과 version 을 추출해 딕셔너리로 반환한다.

    예: "myproj-1.0.0-py3-none-any.whl" →
        {"name": "myproj", "version": "1.0.0"}
    """
    # TODO: filename 에서 .whl 확장자를 제거하고 "-" 로 분리해
    #       첫 번째 요소(name)와 두 번째 요소(version)를 딕셔너리로 반환하세요.
    raise NotImplementedError


if __name__ == "__main__":
    result = parse_wheel_filename("myproj-1.0.0-py3-none-any.whl")
    assert result["name"] == "myproj"
    assert result["version"] == "1.0.0"

    result2 = parse_wheel_filename("requests-2.31.0-py3-none-any.whl")
    assert result2["name"] == "requests"
    assert result2["version"] == "2.31.0"

    print("OK")
