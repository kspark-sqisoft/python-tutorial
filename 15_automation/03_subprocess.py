"""
subprocess 모듈로 외부 프로세스를 실행하고 결과를 캡처하는 방법을 학습한다.
stdout/stderr 캡처, 반환 코드 확인, 오류 처리, 타임아웃을 다룬다.
shell=False 를 유지해 명령 인젝션 취약점을 방지한다.
"""

import subprocess

# ──── 1. 기본 실행 — subprocess.run ────

# capture_output=True : stdout/stderr 를 문자열로 캡처
# text=True           : bytes 대신 str 로 반환
# shell=False (기본값): 셸을 거치지 않아 인젝션 공격 방지 ← 항상 유지할 것
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True,
)

print("=== python --version ===")
print(f"  returncode : {result.returncode}")   # 0 = 정상 종료
print(f"  stdout     : {result.stdout.strip()}")
print(f"  stderr     : {result.stderr.strip()}")

# ──── 2. python -c 로 짧은 코드 실행 ────

result2 = subprocess.run(
    ["python", "-c", "print('subprocess 에서 실행됨')"],
    capture_output=True,
    text=True,
)

print("\n=== python -c 'print(...)' ===")
print(f"  returncode : {result2.returncode}")
print(f"  stdout     : {result2.stdout.strip()}")

# ──── 3. check=True — 비정상 종료 시 CalledProcessError 발생 ────

print("\n=== check=True 오류 처리 ===")
try:
    subprocess.run(
        ["python", "-c", "import sys; sys.exit(1)"],
        capture_output=True,
        text=True,
        check=True,   # returncode != 0 이면 예외 발생
    )
except subprocess.CalledProcessError as e:
    print(f"  CalledProcessError 발생: returncode={e.returncode}")

# ──── 4. timeout — 너무 오래 걸리면 TimeoutExpired ────

# timeout=초 : 지정 시간 초과 시 TimeoutExpired 예외 발생
print("\n=== timeout 예시 ===")
try:
    subprocess.run(
        ["python", "-c", "print('빠른 명령')"],
        capture_output=True,
        text=True,
        timeout=5,   # 5초 안에 끝나야 함
    )
    print("  타임아웃 없이 정상 완료")
except subprocess.TimeoutExpired:
    print("  TimeoutExpired 발생")

# ──── 5. stdout/stderr 분리 확인 ────

result3 = subprocess.run(
    ["python", "-c",
     "import sys; print('표준출력'); print('표준에러', file=sys.stderr)"],
    capture_output=True,
    text=True,
)

print("\n=== stdout / stderr 분리 ===")
print(f"  stdout : {result3.stdout.strip()}")
print(f"  stderr : {result3.stderr.strip()}")


if __name__ == "__main__":
    # 추가 시연: 현재 파이썬 경로 출력
    import sys
    r = subprocess.run(
        [sys.executable, "-c", "import sys; print(sys.version)"],
        capture_output=True,
        text=True,
    )
    print("\n=== 현재 인터프리터 버전 ===")
    print(f"  {r.stdout.strip()}")
