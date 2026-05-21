"""
pathlib 으로 파일 IO — Path.read_text / write_text
한 줄로 파일을 읽고 쓸 수 있는 가장 간결한 방법.
TemporaryDirectory 와 함께 쓰면 잔여물 없이 시연할 수 있다.
"""

import tempfile
from pathlib import Path

# ──── 1. write_text / read_text ────

def demo_text_io(base_dir):
    # Path 객체로 경로를 다루면 os.path 없이도 직관적으로 조합 가능
    file_path = Path(base_dir) / "인사말.txt"

    # write_text: 문자열을 파일에 한 번에 씀 (파일이 없으면 생성)
    file_path.write_text("안녕하세요, pathlib!\n두 번째 줄입니다.", encoding="utf-8")

    # read_text: 파일 전체를 문자열로 반환
    content = file_path.read_text(encoding="utf-8")
    return content


# ──── 2. write_bytes / read_bytes ────

def demo_bytes_io(base_dir):
    bin_path = Path(base_dir) / "data.bin"

    # write_bytes / read_bytes: bytes 객체 그대로 저장/로드
    bin_path.write_bytes(b"\xDE\xAD\xBE\xEF")
    data = bin_path.read_bytes()
    return data


# ──── 3. 경로 조작 유틸리티 ────

def demo_path_operations(base_dir):
    p = Path(base_dir) / "sub" / "report.txt"

    # 부모 디렉터리 자동 생성
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("리포트 내용", encoding="utf-8")

    return {
        "존재": p.exists(),
        "이름": p.name,          # "report.txt"
        "줄기": p.stem,          # "report"
        "확장자": p.suffix,      # ".txt"
        "부모": str(p.parent),
        "절대경로": p.is_absolute(),
    }


# ──── 4. 디렉터리 파일 목록 ────

def demo_glob(base_dir):
    base = Path(base_dir)
    # 여러 텍스트 파일 생성
    (base / "a.txt").write_text("a", encoding="utf-8")
    (base / "b.txt").write_text("b", encoding="utf-8")
    (base / "c.log").write_text("c", encoding="utf-8")

    # glob: 패턴 매칭으로 파일 목록 반환
    txt_files = sorted(p.name for p in base.glob("*.txt"))
    all_files  = sorted(p.name for p in base.iterdir() if p.is_file())
    return txt_files, all_files


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        print("=== write_text / read_text ===")
        content = demo_text_io(tmp_dir)
        print(repr(content))

        print("\n=== write_bytes / read_bytes ===")
        data = demo_bytes_io(tmp_dir)
        print(f"읽은 bytes: {data.hex().upper()}")

        print("\n=== 경로 조작 ===")
        info = demo_path_operations(tmp_dir)
        for k, v in info.items():
            print(f"  {k}: {v}")

        print("\n=== glob ===")
        txt_files, all_files = demo_glob(tmp_dir)
        print(f"*.txt 파일: {txt_files}")
        print(f"전체 파일: {all_files}")

    # with 블록 종료 → TemporaryDirectory 자동 삭제
    print("\nTemporaryDirectory 자동 정리 완료.")
