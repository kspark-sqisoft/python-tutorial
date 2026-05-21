"""
연습 04 — CSV DictWriter / DictReader 왕복
tempfile 에 DictWriter 로 3행을 쓰고 DictReader 로 읽어
행 수와 특정 필드 값을 검증한다. newline="" 를 반드시 사용한다.
"""

import csv
import tempfile
import os

def exercise():
    fd, tmp_path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)

    fieldnames = ["이름", "점수", "등급"]
    rows = [
        {"이름": "홍길동", "점수": "95", "등급": "A"},
        {"이름": "김철수", "점수": "82", "등급": "B"},
        {"이름": "이영희", "점수": "91", "등급": "A"},
    ]

    # TODO: tmp_path 를 newline="", encoding="utf-8" 로 열고
    #       DictWriter 로 헤더와 3행을 쓴다

    # TODO: tmp_path 를 newline="", encoding="utf-8" 로 열고
    #       DictReader 로 모든 행을 읽어 records 리스트에 담는다
    records = []

    assert len(records) == 3, f"행 수가 3이어야 합니다: {len(records)}"
    assert records[0]["이름"] == "홍길동", f"첫 행 이름이 다릅니다: {records[0]}"

    os.unlink(tmp_path)
    print("OK")

if __name__ == "__main__":
    exercise()
