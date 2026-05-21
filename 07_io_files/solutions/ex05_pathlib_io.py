"""
정답 05 — pathlib Path.write_text / read_text 왕복
Path.write_text / read_text 는 open() 없이 한 줄로 파일 IO를 처리한다.
encoding="utf-8" 을 명시해 한글이 깨지지 않게 한다.
TemporaryDirectory 로 with 블록 종료 시 자동 정리된다.
"""

import tempfile
from pathlib import Path

def exercise():
    original = "안녕하세요, pathlib!\n한글 텍스트 왕복 테스트입니다."

    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / "test.txt"

        # 한 줄로 파일 쓰기
        file_path.write_text(original, encoding="utf-8")

        # 한 줄로 파일 읽기
        result = file_path.read_text(encoding="utf-8")

        assert result == original, (
            f"원본과 다릅니다:\n원본: {original!r}\n결과: {result!r}"
        )

    print("OK")

if __name__ == "__main__":
    exercise()
