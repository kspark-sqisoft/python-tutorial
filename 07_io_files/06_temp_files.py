"""
임시 자원 — tempfile 모듈
NamedTemporaryFile 과 TemporaryDirectory 로 잔여물 없는 IO 시연.
학습/테스트 코드에서 실제 경로를 하드코딩하지 않아도 된다.
"""

import tempfile
import os
from pathlib import Path

# ──── 1. NamedTemporaryFile(delete=False) ────

def demo_named_temp_file():
    # delete=False: close 해도 파일이 삭제되지 않아 경로를 재사용할 수 있다
    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".txt",
        mode="w",
        encoding="utf-8",
    )
    tmp_path = tmp.name   # 운영체제가 지정한 임시 경로
    tmp.write("임시 파일 내용\n")
    tmp.close()           # 닫아야 다른 프로세스/코드에서 읽을 수 있다

    # 경로를 알고 있으므로 일반 open 으로 다시 열 수 있다
    with open(tmp_path, "r", encoding="utf-8") as f:
        content = f.read()

    os.unlink(tmp_path)   # 다 쓴 뒤 직접 삭제
    return content, tmp_path


# ──── 2. NamedTemporaryFile(delete=True) — 기본값 ────

def demo_auto_delete():
    # delete=True(기본): close 시 자동 삭제 — 경로 재사용 불가
    # Windows 에서는 열린 채로 다른 프로세스가 읽을 수 없으므로 주의
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=True) as tmp:
        tmp_path = tmp.name
        tmp.write(b"\x01\x02\x03")
        tmp.flush()
        exists_inside = Path(tmp_path).exists()
    exists_outside = Path(tmp_path).exists()
    return exists_inside, exists_outside


# ──── 3. TemporaryDirectory ────

def demo_temp_directory():
    # with 블록 종료 시 디렉터리 전체(하위 파일 포함)가 자동 삭제된다
    captured_path = None
    with tempfile.TemporaryDirectory() as tmp_dir:
        captured_path = tmp_dir
        base = Path(tmp_dir)

        # 디렉터리 안에 파일을 자유롭게 생성
        (base / "note.txt").write_text("노트 내용", encoding="utf-8")
        (base / "sub").mkdir()
        (base / "sub" / "data.txt").write_text("하위 데이터", encoding="utf-8")

        exists_inside = base.exists()

    exists_outside = Path(captured_path).exists()
    return exists_inside, exists_outside, captured_path


# ──── 4. mkstemp / mkdtemp — 저수준 API ────

def demo_low_level():
    # mkstemp: (fd, path) 반환 — fd(파일 디스크립터) 를 직접 관리
    fd, path = tempfile.mkstemp(suffix=".tmp")
    os.close(fd)           # fd 를 닫아야 다른 코드에서 열 수 있다
    Path(path).write_text("mkstemp 내용", encoding="utf-8")
    content = Path(path).read_text(encoding="utf-8")
    os.unlink(path)

    # mkdtemp: 임시 디렉터리 경로 반환 — 삭제를 직접 처리해야 한다
    import shutil
    tmp_dir = tempfile.mkdtemp()
    (Path(tmp_dir) / "file.txt").write_text("mkdtemp 내용", encoding="utf-8")
    shutil.rmtree(tmp_dir)  # 디렉터리와 내용물 모두 삭제

    return content


if __name__ == "__main__":
    print("=== NamedTemporaryFile(delete=False) ===")
    content, used_path = demo_named_temp_file()
    print(f"내용: {repr(content)}")
    print(f"삭제 후 존재: {Path(used_path).exists()}")

    print("\n=== NamedTemporaryFile(delete=True) ===")
    inside, outside = demo_auto_delete()
    print(f"블록 안 존재: {inside}")
    print(f"블록 밖 존재: {outside}")

    print("\n=== TemporaryDirectory ===")
    inside, outside, path = demo_temp_directory()
    print(f"블록 안 존재: {inside}")
    print(f"블록 밖 존재: {outside}")
    print(f"삭제된 경로: {path}")

    print("\n=== mkstemp / mkdtemp ===")
    print(f"mkstemp 내용: {repr(demo_low_level())}")
