"""
with 문 — 컨텍스트 매니저로 안전한 파일 처리
with open(...) as f: 는 예외가 발생해도 파일을 자동으로 닫는다.
여러 파일을 동시에 열 때는 쉼표로 이어 쓴다.
"""

import tempfile
import os

# ──── 1. with 없이 close 누락 위험 ────

def without_with(path):
    # close 전에 예외 발생 시 파일이 열린 채로 남을 수 있다
    f = open(path, "w", encoding="utf-8")
    try:
        f.write("위험한 방식\n")
    finally:
        f.close()  # finally 로 직접 보장해야 하는 번거로움


# ──── 2. with 로 자동 close ────

def with_basic(path):
    # with 블록을 벗어나면 예외 여부에 상관없이 f.close() 가 호출된다
    with open(path, "w", encoding="utf-8") as f:
        f.write("안전한 방식\n")
        f.write("블록 종료 시 자동 close\n")


# ──── 3. 읽기 with ────

def with_read(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    return lines


# ──── 4. 두 파일 동시 열기 ────

def with_two_files(src_path, dst_path):
    # 쉼표로 여러 컨텍스트 매니저를 한 줄에 선언
    with open(src_path, "r", encoding="utf-8") as src, \
         open(dst_path, "w", encoding="utf-8") as dst:
        for line in src:
            # 각 줄을 대문자로 변환해 출력 파일에 쓴다
            dst.write(line.upper())


# ──── 5. 추가 모드(a)와 with ────

def with_append(path):
    with open(path, "a", encoding="utf-8") as f:
        f.write("추가된 줄\n")


# ──── 6. 컨텍스트 매니저 직접 구현 안내 ────

# __enter__ / __exit__ 를 정의하거나 contextlib.contextmanager 를 쓰면
# 직접 만들 수 있다. 자세한 내용은 09_advanced_python 에서 다룬다.

if __name__ == "__main__":
    # 임시 파일 두 개 생성
    fd_src, src_path = tempfile.mkstemp(suffix=".txt")
    os.close(fd_src)
    fd_dst, dst_path = tempfile.mkstemp(suffix=".txt")
    os.close(fd_dst)

    print("=== with 기본 쓰기 ===")
    with_basic(src_path)
    print(with_read(src_path))

    print("\n=== 두 파일 동시 열기 — 대문자 변환 복사 ===")
    # 원본에 여러 줄 작성
    with open(src_path, "w", encoding="utf-8") as f:
        f.write("hello python\n")
        f.write("with statement\n")
        f.write("컨텍스트 매니저\n")

    with_two_files(src_path, dst_path)
    result = with_read(dst_path)
    print(result)

    print("\n=== 추가 모드 ===")
    with_append(dst_path)
    print(with_read(dst_path))

    # 임시 파일 정리
    os.unlink(src_path)
    os.unlink(dst_path)
    print("\n임시 파일 정리 완료.")
