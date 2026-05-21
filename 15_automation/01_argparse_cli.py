"""
argparse 모듈로 CLI(명령줄 인터페이스)를 만드는 방법을 학습한다.
표준 라이브러리만 사용하므로 별도 설치 없이 바로 실행 가능하다.
ArgumentParser, 옵션 인수, 위치 인수, 타입 변환을 다룬다.
"""

import argparse

# ──── 1. 기본 파서 생성 ────

# ArgumentParser 는 프로그램 설명과 도움말을 자동으로 생성해 준다
parser = argparse.ArgumentParser(
    description="인사 CLI — 이름과 횟수를 받아 인사를 반복한다",
    epilog="예시: python 01_argparse_cli.py --name 홍길동 --count 3",
)

# ──── 2. 옵션 인수 등록 (--flag 형태) ────

# --name: 문자열 옵션, 기본값 "World"
parser.add_argument(
    "--name",
    default="World",
    help="인사할 대상 이름 (기본값: World)",
)

# --count: 정수 옵션, type=int 로 자동 형 변환
parser.add_argument(
    "--count",
    type=int,
    default=1,
    help="인사 반복 횟수 (기본값: 1)",
)

# ──── 3. 위치 인수 등록 (플래그 없이 순서로 받는 인수) ────

# 위치 인수는 nargs="?" 로 선택적으로 만들 수 있다
parser.add_argument(
    "input_file",
    nargs="?",           # 0개 또는 1개 — 선택적 위치 인수
    default="없음",
    help="처리할 파일 경로 (선택)",
)

# ──── 4. parse_args — 인수 목록을 직접 전달 (대화형 입력 X) ────

# 실제 CLI 에서는 parse_args() 를 인수 없이 호출하지만,
# 학습·테스트 환경에서는 리스트를 직접 전달한다
args = parser.parse_args(["--name", "Kee", "--count", "3"])

print("=== parse_args 결과 ===")
print(f"  name      : {args.name}")
print(f"  count     : {args.count}")
print(f"  input_file: {args.input_file}")
print(f"  타입 확인  : count 는 {type(args.count).__name__}")

# ──── 5. 파싱 결과 활용 예시 ────

print("\n=== 인사 출력 ===")
for i in range(args.count):
    print(f"  [{i+1}] 안녕하세요, {args.name}!")

# ──── 6. 다른 인수 조합 시연 ────

args2 = parser.parse_args(["--count", "2", "data.csv"])
print("\n=== 위치 인수 포함 파싱 ===")
print(f"  name      : {args2.name}")   # 기본값 "World"
print(f"  count     : {args2.count}")
print(f"  input_file: {args2.input_file}")

if __name__ == "__main__":
    # 도움말 출력 (--help 와 동일)
    print("\n=== 자동 생성 도움말 ===")
    parser.print_help()
