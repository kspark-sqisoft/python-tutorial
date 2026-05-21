"""
정답 05 — wheel 파일 이름 파싱
parse_wheel_filename 함수 구현.
"""


def parse_wheel_filename(filename: str) -> dict[str, str]:
    """wheel 파일 이름에서 name 과 version 을 추출해 딕셔너리로 반환한다.

    예: "myproj-1.0.0-py3-none-any.whl" →
        {"name": "myproj", "version": "1.0.0"}
    """
    stem = filename.removesuffix(".whl")
    parts = stem.split("-")
    return {"name": parts[0], "version": parts[1]}


if __name__ == "__main__":
    result = parse_wheel_filename("myproj-1.0.0-py3-none-any.whl")
    assert result["name"] == "myproj"
    assert result["version"] == "1.0.0"

    result2 = parse_wheel_filename("requests-2.31.0-py3-none-any.whl")
    assert result2["name"] == "requests"
    assert result2["version"] == "2.31.0"

    print("OK")
