"""
연습 02 — with 문으로 두 파일 동시 처리
입력 파일에 "hello\nworld" 를 쓰고,
with open(in) as i, open(out, "w") as o: 패턴으로
각 줄을 upper() 변환해 출력 파일에 저장한다.
"""

import tempfile
import os

def exercise():
    # 임시 파일 두 개 경로 확보
    fd_in, in_path  = tempfile.mkstemp(suffix=".txt")
    os.close(fd_in)
    fd_out, out_path = tempfile.mkstemp(suffix=".txt")
    os.close(fd_out)

    # TODO: in_path 에 "hello\nworld\n" 을 write 모드(encoding="utf-8")로 쓴다

    # TODO: with open(in_path, "r", ...) as fin, open(out_path, "w", ...) as fout:
    #        fin 의 각 줄을 upper() 변환해 fout 에 쓴다

    # 검증
    with open(out_path, "r", encoding="utf-8") as f:
        result = [line.rstrip("\n") for line in f]

    assert result == ["HELLO", "WORLD"], f"기대값과 다릅니다: {result}"

    # 임시 파일 정리
    os.unlink(in_path)
    os.unlink(out_path)
    print("OK")

if __name__ == "__main__":
    exercise()
