"""
정답 02 — with 문으로 두 파일 동시 처리
with open(in) as fin, open(out, "w") as fout: 로
두 파일을 한 블록에서 열어 줄 단위 upper() 변환을 수행한다.
with 블록이 끝나면 두 파일 모두 자동으로 닫힌다.
"""

import tempfile
import os

def exercise():
    fd_in, in_path  = tempfile.mkstemp(suffix=".txt")
    os.close(fd_in)
    fd_out, out_path = tempfile.mkstemp(suffix=".txt")
    os.close(fd_out)

    # 입력 파일 작성
    with open(in_path, "w", encoding="utf-8") as f:
        f.write("hello\nworld\n")

    # 두 파일 동시 열기 — 각 줄 upper() 변환
    with open(in_path, "r", encoding="utf-8") as fin, \
         open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            fout.write(line.upper())

    # 검증
    with open(out_path, "r", encoding="utf-8") as f:
        result = [line.rstrip("\n") for line in f]

    assert result == ["HELLO", "WORLD"], f"기대값과 다릅니다: {result}"

    os.unlink(in_path)
    os.unlink(out_path)
    print("OK")

if __name__ == "__main__":
    exercise()
