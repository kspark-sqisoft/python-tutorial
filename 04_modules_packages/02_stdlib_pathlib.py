"""pathlib 으로 파일 시스템 경로를 다루는 방법을 익힌다.
문자열 대신 Path 객체를 사용하면 OS 에 관계없이 안전하게 경로를 처리할 수 있다.
/ 연산자로 경로를 결합하고, 다양한 속성으로 경로 정보를 추출한다.
"""

from pathlib import Path  # 표준 라이브러리 pathlib 에서 Path 클래스를 가져온다

# ──── 1. 기본 경로 ────
cwd = Path.cwd()        # 현재 작업 디렉터리
home = Path.home()      # 사용자 홈 디렉터리
this = Path(__file__)   # 현재 실행 중인 파일의 경로

# ──── 2. 경로 결합 ────
combined = cwd / "sub" / "file.txt"  # / 연산자로 경로 조각을 이어 붙인다

# ──── 3. 경로 속성 ────
# .name   — 파일명(확장자 포함)
# .stem   — 파일명(확장자 제외)
# .suffix — 확장자 (.py, .txt 등)
# .parent — 부모 디렉터리

# ──── 4. 존재 여부 확인 ────
# .exists()   — 경로가 존재하면 True
# .is_file()  — 파일이면 True
# .is_dir()   — 디렉터리이면 True

# ──── 5. 디렉터리 순회 ────
# list(p.iterdir()) — 디렉터리 내 모든 항목 목록
# p.glob("*.py")    — 패턴에 맞는 파일만

if __name__ == "__main__":
    print(f"현재 파일: {this}")
    print(f"부모 디렉터리: {this.parent}")
    print(f"파일 이름: {this.name}")
    print(f"확장자: {this.suffix}")
    print(f"확장자 제외 이름: {this.stem}")
    print()
    print(f"현재 작업 디렉터리: {cwd}")
    print(f"홈 디렉터리: {home}")
    print()
    print(f"이 파일 존재?: {this.exists()}")
    print(f"파일?: {this.is_file()}")
    print(f"디렉터리?: {this.is_dir()}")
    print()

    # 부모 디렉터리의 .py 파일 목록
    py_files = sorted(this.parent.glob("*.py"))
    print(f"같은 폴더의 .py 파일 수: {len(py_files)}")
    for f in py_files:
        print(f"  {f.name}")
