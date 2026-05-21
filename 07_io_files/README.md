# 07_io_files — 파일 입출력

## 배우는 것
- open() 기본 (r/w/a/rb/wb, encoding="utf-8")
- with 문으로 안전한 자원 정리
- JSON 직렬화/역직렬화 (한글: ensure_ascii=False)
- CSV reader/writer + DictReader/DictWriter (newline="")
- pathlib 의 read_text / write_text
- tempfile 로 안전한 임시 자원

## 학습 순서
1. `01_open_read_write.py`
2. `02_with_statement.py`
3. `03_json.py`
4. `04_csv.py`
5. `05_pathlib_io.py`
6. `06_temp_files.py`

## 실행 방법
```bash
uv run python 07_io_files/01_open_read_write.py
```

## 연습문제
- `exercises/ex01_*.py` ~ `ex06_*.py` 의 TODO를 채워 `OK` 가 출력되게 만든다.
- 모든 학습·연습은 임시 파일/디렉터리에서만 작업하므로 저장소에 잔여물이 남지 않는다.
