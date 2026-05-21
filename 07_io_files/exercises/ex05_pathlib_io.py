"""
연습 05 — pathlib Path.write_text / read_text 왕복
TemporaryDirectory 안에 Path 로 한글 포함 텍스트를 쓰고
다시 읽어 원본과 동일한지 확인한다.
"""

import tempfile
from pathlib import Path

def exercise():
    original = "안녕하세요, pathlib!\n한글 텍스트 왕복 테스트입니다."

    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / "test.txt"

        # TODO: file_path.write_text(original, encoding="utf-8") 로 파일을 쓴다

        # TODO: file_path.read_text(encoding="utf-8") 로 파일을 읽어 result 에 담는다
        result = None

        assert result == original, f"원본과 다릅니다:\n원본: {original!r}\n결과: {result!r}"

    print("OK")

if __name__ == "__main__":
    exercise()
