"""
정답 01 — open() 기본 읽기/쓰기
NamedTemporaryFile(delete=False) 로 경로를 확보한 뒤
"w" 모드로 두 줄을 쓰고, "r" 모드 for line 반복으로 읽는다.
마지막에 unlink() 로 파일을 직접 삭제해 잔여물을 남기지 않는다.
"""

import tempfile
import os
from pathlib import Path

def exercise():
    # delete=False: close 후에도 파일이 남아 경로를 재사용할 수 있다
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    tmp_path = tmp.name
    tmp.close()

    # "w" 모드로 두 줄 쓰기
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write("안녕\n")
        f.write("반가워\n")

    # for line in f: — 가장 권장하는 읽기 방식
    lines = []
    with open(tmp_path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.rstrip("\n"))

    assert len(lines) == 2, f"줄 수가 2여야 합니다. 현재: {len(lines)}"

    # 임시 파일 삭제
    Path(tmp_path).unlink()
    print("OK")

if __name__ == "__main__":
    exercise()
