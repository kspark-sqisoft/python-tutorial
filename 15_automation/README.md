# 15_automation — 자동화·스크립팅

## 사전 준비

```bash
uv pip install -e ".[auto]"
```

## 배우는 것

- argparse — 표준 라이브러리 CLI
- click — 데코레이터 기반 CLI (CliRunner 로 테스트)
- subprocess — 외부 명령 (shell=False, capture_output)
- BeautifulSoup — HTML 파싱 (로컬 문자열로 시연)
- pathlib + shutil — 파일/디렉터리 자동화 (tempfile 안에서)

## 학습 순서

1. `01_argparse_cli.py`
2. `02_click_cli.py`
3. `03_subprocess.py`
4. `04_beautifulsoup.py`
5. `05_os_pathlib_automation.py`

## 실행 방법

```bash
uv run python 15_automation/01_argparse_cli.py
uv run python 15_automation/02_click_cli.py
uv run python 15_automation/03_subprocess.py
uv run python 15_automation/04_beautifulsoup.py
uv run python 15_automation/05_os_pathlib_automation.py
```

## 연습문제

`exercises/` 의 TODO 를 채우고, `solutions/` 와 비교한다.

- 외부 네트워크 / 시스템 변경 X — 모든 IO 는 임시 자원, HTML 은 로컬 문자열.

```bash
uv run python 15_automation/solutions/ex01_argparse_cli.py
uv run python 15_automation/solutions/ex02_click_cli.py
uv run python 15_automation/solutions/ex03_subprocess.py
uv run python 15_automation/solutions/ex04_beautifulsoup.py
uv run python 15_automation/solutions/ex05_os_pathlib_automation.py
```
