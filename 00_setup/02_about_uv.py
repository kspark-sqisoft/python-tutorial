"""자주 쓸 uv 명령어 정리.

uv 는 Rust 로 만든 파이썬 패키지 관리자다 (pip + venv + pyenv 역할을 한 도구로 통합).
이 파일은 실제로 uv 를 부르지 않고, 명령어를 문자열로 출력만 한다.
실행하면 "어떤 명령을 어떤 상황에서 쓰는가" 를 한눈에 볼 수 있다.
"""

import sys                              # 표준 라이브러리. 인터프리터 정보를 얻을 때 쓴다.


# ──── 1. 현재 파이썬 환경 확인 ────

# sys.executable 은 지금 실행 중인 파이썬 인터프리터의 경로다.
# `uv run python ...` 으로 돌렸다면 `.venv/bin/python` 비슷한 경로가 나온다.
print(f"인터프리터 경로: {sys.executable}")
print(f"파이썬 버전:     {sys.version.split()[0]}")


# ──── 2. 알아둘 uv 명령 ────

# 학습 중 가장 자주 쓰게 될 명령들 — 단순 문자열로 안내만 한다.
commands = [
    ("uv venv",                        "가상환경(.venv)을 만든다. uv sync 가 자동으로 호출하므로 보통 직접 칠 일은 없다."),
    ("uv sync",                        "pyproject.toml 의 dependencies 를 .venv 에 동기화한다."),
    ("uv pip install -e \".[data]\"",  "선택 그룹(data)을 추가 설치한다. Phase 4 진입 시 사용."),
    ("uv run python <파일>",            "가상환경을 자동 활성화해서 파이썬 스크립트를 실행한다."),
    ("uv add <패키지>",                  "새 의존성을 추가하고 pyproject.toml 에 기록한다."),
    ("uv remove <패키지>",               "의존성을 제거한다."),
    ("uv lock",                        "잠금 파일(uv.lock)을 갱신한다. 재현 가능한 환경을 위해."),
]

# 보기 좋게 표로 출력 — f-string 안의 `:<28` 는 28칸 너비 왼쪽 정렬을 뜻한다.
for cmd, desc in commands:
    print(f"  {cmd:<28} {desc}")


# ──── 데모 실행 ────
if __name__ == "__main__":
    print("---")
    print("이 단원은 끝났습니다. 다음 폴더: 01_basics/")
