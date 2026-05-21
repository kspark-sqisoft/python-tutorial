"""
CSV 읽기/쓰기 — csv 모듈
reader/writer 는 리스트 기반, DictReader/DictWriter 는 dict 기반.
newline="" 옵션은 Windows 호환을 위해 항상 지정한다.
"""

import csv
import tempfile
import os

# ──── 1. csv.writer / csv.reader — 리스트 기반 ────

def demo_writer_reader(path):
    # newline="": csv 모듈이 줄 끝을 직접 관리하게 한다 (Windows \r\n 이중 삽입 방지)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["이름", "나이", "도시"])       # 헤더
        writer.writerow(["홍길동", 30, "서울"])
        writer.writerow(["김철수", 25, "부산"])
        writer.writerow(["이영희", 28, "대전"])

    rows = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows


# ──── 2. csv.DictWriter / csv.DictReader — dict 기반 ────

def demo_dict_writer_reader(path):
    fieldnames = ["상품", "가격", "재고"]
    data = [
        {"상품": "사과", "가격": 1500, "재고": 100},
        {"상품": "바나나", "가격": 800, "재고": 250},
        {"상품": "오렌지", "가격": 2000, "재고": 60},
    ]

    with open(path, "w", newline="", encoding="utf-8") as f:
        # extrasaction="raise": 지정한 fieldnames 외의 키가 있으면 오류
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()          # 첫 행에 필드명 자동 작성
        writer.writerows(data)        # 리스트 한 번에 쓰기

    records = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)    # 첫 행을 fieldnames 로 자동 인식
        for row in reader:
            records.append(dict(row))
    return records


# ──── 3. 특수 구분자 ────

def demo_delimiter(path):
    # delimiter="\t" 로 TSV(탭 구분) 형식도 처리 가능
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["코드", "설명"])
        writer.writerow(["A001", "첫 번째 항목"])
        writer.writerow(["B002", "두 번째 항목"])

    rows = []
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            rows.append(row)
    return rows


if __name__ == "__main__":
    fd, tmp_path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)

    print("=== writer / reader (리스트) ===")
    rows = demo_writer_reader(tmp_path)
    for r in rows:
        print(r)

    print("\n=== DictWriter / DictReader ===")
    records = demo_dict_writer_reader(tmp_path)
    for rec in records:
        print(rec)

    print("\n=== 탭 구분자 ===")
    tsv_rows = demo_delimiter(tmp_path)
    for r in tsv_rows:
        print(r)

    os.unlink(tmp_path)
    print("\n임시 파일 정리 완료.")
