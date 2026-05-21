"""정답 05 — pathlib + glob + tempfile"""

import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp_str:
    tmp = Path(tmp_str)

    # .txt 3개 + .log 1개 생성
    for name in ["a.txt", "b.txt", "c.txt"]:
        (tmp / name).write_text(f"{name} 내용", encoding="utf-8")
    (tmp / "debug.log").write_text("로그", encoding="utf-8")

    # .txt 만 수집
    txt_files = list(tmp.glob("*.txt"))

    assert len(txt_files) == 3
    assert all(f.suffix == ".txt" for f in txt_files)
    print("OK")
