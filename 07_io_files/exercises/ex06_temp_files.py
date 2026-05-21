"""
연습 06 — TemporaryDirectory 생명주기 확인
with 블록 안에서 .exists() == True,
블록 종료 후 .exists() == False 두 가지를 assert 한다.
"""

import tempfile
from pathlib import Path

def exercise():
    captured_path = None

    # TODO: tempfile.TemporaryDirectory() 를 with 문으로 열고
    #       tmp_dir 경로를 captured_path 변수에 저장한다

    # TODO: with 블록 안에서 Path(captured_path).exists() == True 를 assert 한다

    # (with 블록 종료 후)
    # TODO: Path(captured_path).exists() == False 를 assert 한다

    assert captured_path is not None, "captured_path 를 설정하세요"

    print("OK")

if __name__ == "__main__":
    exercise()
