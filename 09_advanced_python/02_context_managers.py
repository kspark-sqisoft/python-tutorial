"""
컨텍스트 매니저(Context Manager) 학습 모듈.
with 문의 원리(__enter__ / __exit__)를 이해하고,
클래스 기반과 @contextmanager 두 가지 구현 방법을 다룬다.
"""

import time
import os
from contextlib import contextmanager

# ──── 1. with 문의 원리 ────

# with expr as name:
#     블록
# 은 아래와 동일하다:
#   mgr = expr
#   name = mgr.__enter__()
#   try:
#       블록
#   except:
#       if not mgr.__exit__(exc_type, exc_val, exc_tb):
#           raise
#   else:
#       mgr.__exit__(None, None, None)


# ──── 2. 클래스 기반 컨텍스트 매니저 ────

class Timer:
    """코드 블록의 실행 시간을 측정하는 컨텍스트 매니저."""

    def __enter__(self):
        self._start = time.perf_counter()   # 진입 시 시작 시각 저장
        return self                          # as 절에 self 가 바인딩됨

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self._start
        print(f"[Timer] 경과 시간: {elapsed:.4f}초")
        # False(또는 None) 반환 → 예외를 삼키지 않고 그대로 전파
        return False


# ──── 3. 예외 처리 — __exit__ 의 매개변수 ────

# __exit__(exc_type, exc_val, exc_tb)
#   - 정상 종료 시: 세 인자 모두 None
#   - 예외 발생 시: exc_type = 예외 클래스, exc_val = 예외 인스턴스
#   - True 를 반환하면 예외를 삼킴(suppress), False/None 이면 예외 전파

class SuppressZeroDivision:
    """ZeroDivisionError 를 조용히 무시하는 예시 컨텍스트 매니저."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("[SuppressZeroDivision] 0으로 나누기 무시됨")
            return True     # 예외 삼킴
        return False        # 다른 예외는 그대로 전파


# ──── 4. 함수 기반 — @contextmanager ────

# contextlib.contextmanager 를 사용하면 제너레이터 함수로 컨텍스트 매니저를 만들 수 있다
# yield 이전: __enter__ 역할 (setup)
# yield 이후: __exit__ 역할 (cleanup)

@contextmanager
def working_directory(path):
    """일시적으로 작업 디렉터리를 변경하고 블록 종료 후 원복."""
    original = os.getcwd()      # 현재 디렉터리 저장
    os.chdir(path)              # 지정 경로로 이동 (setup)
    try:
        yield path              # as 절에 path 가 바인딩됨
    finally:
        os.chdir(original)      # 항상 원복 (cleanup) — 예외가 발생해도 실행됨


@contextmanager
def tag(name):
    """HTML 태그로 감싸는 간단한 예시."""
    print(f"<{name}>", end="")  # setup
    yield                        # 블록 실행
    print(f"</{name}>")         # cleanup


# ──── 5. 중첩 컨텍스트 매니저 ────

# with A() as a, B() as b:  는  with A() as a:  with B() as b: 와 동일


if __name__ == "__main__":
    # 클래스 기반 Timer 시연
    print("=== Timer (클래스 기반) ===")
    with Timer() as t:
        total = sum(range(1_000_000))   # 시간이 걸리는 작업
    print(f"합계: {total}")

    print()

    # SuppressZeroDivision — 예외 삼킴 시연
    print("=== SuppressZeroDivision ===")
    with SuppressZeroDivision():
        x = 1 / 0   # 이 예외는 무시됨
    print("with 블록 이후 정상 실행")

    print()

    # @contextmanager — working_directory 시연
    print("=== working_directory (@contextmanager) ===")
    before = os.getcwd()
    with working_directory("/tmp") as path:
        print(f"블록 안 cwd: {os.getcwd()}")
    print(f"블록 밖 cwd 복원: {os.getcwd() == before}")

    print()

    # tag 시연
    print("=== tag (@contextmanager) ===")
    with tag("b"):
        print("굵은 텍스트", end="")
