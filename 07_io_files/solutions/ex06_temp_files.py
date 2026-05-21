"""
정답 06 — TemporaryDirectory 생명주기 확인
with 블록 안에서 디렉터리가 존재하고,
블록 종료 후 자동으로 삭제되는 것을 assert 로 검증한다.
captured_path 변수로 블록 밖에서도 경로를 참조할 수 있다.
"""

import tempfile
from pathlib import Path

def exercise():
    captured_path = None

    with tempfile.TemporaryDirectory() as tmp_dir:
        # 경로를 블록 밖에서 참조하기 위해 캡처
        captured_path = tmp_dir

        # 블록 안: 디렉터리가 존재해야 한다
        assert Path(captured_path).exists(), "블록 안에서 디렉터리가 존재해야 합니다"

    # 블록 종료 후: 디렉터리가 자동 삭제된다
    assert not Path(captured_path).exists(), "블록 종료 후 디렉터리가 삭제되어야 합니다"

    print("OK")

if __name__ == "__main__":
    exercise()
