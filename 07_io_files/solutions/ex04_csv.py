"""
정답 04 — CSV DictWriter / DictReader 왕복
newline="" 을 지정해 Windows 에서 \r\n 이 이중으로 삽입되는 것을 방지한다.
DictWriter.writeheader() 로 첫 행에 필드명을 자동 작성한다.
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

    # DictWriter 로 헤더 + 3행 쓰기
    with open(tmp_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # DictReader 로 읽기
    records = []
    with open(tmp_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(dict(row))

    assert len(records) == 3, f"행 수가 3이어야 합니다: {len(records)}"
    assert records[0]["이름"] == "홍길동", f"첫 행 이름이 다릅니다: {records[0]}"

    os.unlink(tmp_path)
    print("OK")

if __name__ == "__main__":
    exercise()
