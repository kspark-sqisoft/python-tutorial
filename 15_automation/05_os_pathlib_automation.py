"""
pathlib 과 shutil 로 파일·디렉터리를 자동화하는 방법을 학습한다.
glob/rglob 패턴 매칭, 복사·이동·삭제, tempfile 안전 시연을 다룬다.
모든 파일 조작은 TemporaryDirectory 안에서만 수행해 실제 시스템에 영향을 주지 않는다.
"""

import shutil
import tempfile
from pathlib import Path

# ──── 1. TemporaryDirectory — 안전한 샌드박스 ────

# with 블록을 벗어나면 자동으로 삭제된다 → 실제 파일 시스템에 잔재 없음
with tempfile.TemporaryDirectory() as tmp_str:
    tmp = Path(tmp_str)   # str → Path 객체로 변환
    print(f"=== 임시 디렉터리: {tmp} ===")

    # ──── 2. 파일 생성 ────

    # .txt 파일 3개 + .log 파일 1개 생성
    for name in ["alpha.txt", "beta.txt", "gamma.txt"]:
        (tmp / name).write_text(f"{name} 내용입니다.", encoding="utf-8")

    (tmp / "debug.log").write_text("로그 내용", encoding="utf-8")

    # 서브디렉터리에 .py 파일 1개
    sub = tmp / "scripts"
    sub.mkdir()
    (sub / "helper.py").write_text("# 헬퍼 스크립트", encoding="utf-8")

    print("생성된 파일:")
    for f in tmp.rglob("*"):   # 재귀 전체 탐색
        if f.is_file():
            print(f"  {f.relative_to(tmp)}")

    # ──── 3. glob — 패턴으로 파일 필터링 ────

    # p.glob("*.txt") : 현재 디렉터리에서만 .txt 검색
    txt_files = list(tmp.glob("*.txt"))
    print(f"\n=== glob('*.txt') — {len(txt_files)}개 ===")
    for f in sorted(txt_files):
        print(f"  {f.name}")

    # p.rglob("*.py") : 하위 디렉터리까지 재귀 검색
    py_files = list(tmp.rglob("*.py"))
    print(f"\n=== rglob('*.py') — {len(py_files)}개 ===")
    for f in py_files:
        print(f"  {f.relative_to(tmp)}")

    # ──── 4. shutil.copy — 파일 복사 ────

    dest_dir = tmp / "backup"
    dest_dir.mkdir()

    # shutil.copy(src, dst) : 파일 내용 + 권한 복사 (메타데이터 제외)
    for txt in txt_files:
        shutil.copy(txt, dest_dir / txt.name)

    print(f"\n=== shutil.copy — backup/ 에 복사된 파일 ===")
    for f in sorted(dest_dir.glob("*")):
        print(f"  {f.name}")

    # ──── 5. shutil.move — 파일 이동 ────

    moved_dir = tmp / "moved"
    moved_dir.mkdir()

    # shutil.move(src, dst) : 이동 후 원본 삭제
    shutil.move(str(tmp / "debug.log"), str(moved_dir / "debug.log"))
    print(f"\n=== shutil.move — moved/ 에 이동 ===")
    print(f"  원본 존재 여부: {(tmp / 'debug.log').exists()}")   # False
    print(f"  이동 후 존재  : {(moved_dir / 'debug.log').exists()}")  # True

    # ──── 6. shutil.rmtree — 디렉터리 통째로 삭제 ────

    # shutil.rmtree(path) : 디렉터리와 그 안의 모든 파일 삭제
    shutil.rmtree(dest_dir)
    print(f"\n=== shutil.rmtree — backup/ 삭제 ===")
    print(f"  backup/ 존재 여부: {dest_dir.exists()}")   # False

    # ──── 7. Path 유용한 속성들 ────

    sample = txt_files[0]
    print(f"\n=== Path 속성 예시 ({sample.name}) ===")
    print(f"  .name   : {sample.name}")       # 파일명 + 확장자
    print(f"  .stem   : {sample.stem}")       # 확장자 제외 파일명
    print(f"  .suffix : {sample.suffix}")     # 확장자
    print(f"  .parent : {sample.parent.name}")  # 부모 디렉터리명
    print(f"  .stat().st_size : {sample.stat().st_size} bytes")


if __name__ == "__main__":
    # 임시 디렉터리는 with 블록 종료 시 이미 삭제되었음을 확인
    print("\n=== with 블록 종료 후 ===")
    print(f"  임시 디렉터리 존재 여부: {Path(tmp_str).exists()}")
