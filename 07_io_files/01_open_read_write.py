"""
파일 열기/읽기/쓰기 기초 — open() 함수
open(path, mode, encoding) 의 다양한 모드와
read / readline / readlines / for line 반복 비교.
항상 encoding="utf-8" 을 명시한다.
"""

import tempfile
import os

# ──── 1. 쓰기 모드 "w" ────

def demo_write(path):
    # "w" 모드: 파일 새로 생성(기존 내용 삭제)
    f = open(path, "w", encoding="utf-8")
    f.write("첫 번째 줄\n")
    f.write("두 번째 줄\n")
    f.write("세 번째 줄\n")
    f.close()  # 반드시 닫아야 버퍼가 플러시된다


# ──── 2. 추가 모드 "a" ────

def demo_append(path):
    # "a" 모드: 파일 끝에 이어쓰기
    f = open(path, "a", encoding="utf-8")
    f.write("네 번째 줄(추가)\n")
    f.close()


# ──── 3. 읽기 모드 비교 ────

def demo_read_all(path):
    # read(): 파일 전체를 하나의 문자열로 반환
    f = open(path, "r", encoding="utf-8")
    content = f.read()
    f.close()
    return content


def demo_readline(path):
    # readline(): 한 줄씩 읽음 — 줄 끝 \n 포함
    lines = []
    f = open(path, "r", encoding="utf-8")
    while True:
        line = f.readline()
        if not line:   # EOF 이면 빈 문자열 반환
            break
        lines.append(line.rstrip("\n"))
    f.close()
    return lines


def demo_readlines(path):
    # readlines(): 모든 줄을 리스트로 반환 — 메모리에 전부 올라감
    f = open(path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    return [l.rstrip("\n") for l in lines]


def demo_for_loop(path):
    # for line in f: — 가장 권장하는 방식 (메모리 효율적)
    lines = []
    f = open(path, "r", encoding="utf-8")
    for line in f:
        lines.append(line.rstrip("\n"))
    f.close()
    return lines


# ──── 4. 바이너리 모드 "rb" / "wb" ────

def demo_binary(path):
    # "wb": bytes 쓰기, "rb": bytes 읽기
    bin_path = path + ".bin"
    f = open(bin_path, "wb")
    f.write(b"\x00\x01\x02\x03")
    f.close()

    f = open(bin_path, "rb")
    data = f.read()
    f.close()
    return data, bin_path


# ──── 5. writelines ────

def demo_writelines(path):
    # writelines(): 문자열 목록을 연속으로 씀 — \n 는 직접 포함해야 함
    lines = ["알파\n", "베타\n", "감마\n"]
    f = open(path, "w", encoding="utf-8")
    f.writelines(lines)
    f.close()


if __name__ == "__main__":
    # tempfile.NamedTemporaryFile 로 임시 파일 경로 확보
    tmp = tempfile.NamedTemporaryFile(
        delete=False, suffix=".txt", mode="w", encoding="utf-8"
    )
    tmp_path = tmp.name
    tmp.close()  # 경로만 얻고 바로 닫음 (Windows 호환)

    print("=== 쓰기 / 추가 ===")
    demo_write(tmp_path)
    demo_append(tmp_path)

    print("=== read() ===")
    print(repr(demo_read_all(tmp_path)))

    print("\n=== readline() ===")
    print(demo_readline(tmp_path))

    print("\n=== readlines() ===")
    print(demo_readlines(tmp_path))

    print("\n=== for line in f (권장) ===")
    print(demo_for_loop(tmp_path))

    print("\n=== writelines ===")
    demo_writelines(tmp_path)
    print(demo_for_loop(tmp_path))

    print("\n=== 바이너리 ===")
    data, bin_path = demo_binary(tmp_path)
    print(f"읽은 bytes: {data}")

    # 임시 파일 정리
    os.unlink(tmp_path)
    os.unlink(bin_path)
    print("\n임시 파일 정리 완료.")
