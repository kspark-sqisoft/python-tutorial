"""
연습 01 — open() 기본 읽기/쓰기
tempfile 로 임시 파일을 만들고, 두 줄을 쓴 뒤
for line in f: 로 읽어 줄 수가 2인지 확인한다.
"""

import tempfile
import os
from pathlib import Path

def exercise():
    # TODO: NamedTemporaryFile(delete=False, suffix=".txt") 로 임시 파일 경로를 얻는다
    tmp = None
    tmp_path = None

    # TODO: tmp_path 에 "안녕\n반가워\n" 두 줄을 write 모드(encoding="utf-8")로 쓴다

    # TODO: for line in f: 로 줄을 읽어 lines 리스트에 담는다
    lines = []

    # TODO: 줄 수가 2인지 assert 한다
    assert len(lines) == 2, f"줄 수가 2여야 합니다. 현재: {len(lines)}"

    # TODO: Path(tmp_path).unlink() 로 임시 파일을 삭제한다
    print("OK")

if __name__ == "__main__":
    exercise()
