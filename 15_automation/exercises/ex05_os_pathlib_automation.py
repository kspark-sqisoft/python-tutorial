"""
연습문제 05 — pathlib + glob + tempfile

TODO:
1. tempfile.TemporaryDirectory() 를 with 문으로 열어라.
2. 임시 디렉터리 안에 .txt 파일 3개와 .log 파일 1개를 생성하라.
3. Path.glob("*.txt") 로 .txt 파일만 수집하라.
4. 수집된 .txt 파일 개수가 3 임을 assert 로 검증하라.
5. .log 파일이 glob 결과에 포함되지 않음을 assert 로 검증하라.
"""

import tempfile
from pathlib import Path

# ── 여기에 코드를 작성하세요 ──
# with tempfile.TemporaryDirectory() as tmp_str:
#     tmp = Path(tmp_str)
#     ...


# 검증은 with 블록 안에서 수행하세요.
# assert len(txt_files) == 3
# assert all(f.suffix == ".txt" for f in txt_files)
# print("OK")
