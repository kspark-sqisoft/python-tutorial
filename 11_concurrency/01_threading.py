"""
threading 모듈 기초.
Thread 생성·시작·조인, GIL 의 의미,
Lock 으로 공유 자원을 보호하는 방법을 다룬다.
IO-bound 작업에서 스레드가 효과적인 이유를 시간 측정으로 확인한다.
"""

import time
from threading import Thread, Lock

# ──── 1. Thread 생성과 실행 ────

def sleep_worker(name: str, seconds: float) -> None:
    """주어진 시간만큼 sleep 하는 단순 작업자."""
    # 스레드 내부에서 실행되는 함수
    time.sleep(seconds)
    print(f"  [{name}] {seconds}s sleep 완료")


# ──── 2. GIL (Global Interpreter Lock) ────

# CPython 의 GIL: 한 순간에 하나의 스레드만 파이썬 바이트코드 실행 가능.
# → CPU-bound 작업(순수 계산)은 멀티스레드로 병렬화 불가.
# → IO-bound 작업(sleep, 네트워크, 파일 IO)은 대기 중 GIL 해제 → 효과적.


# ──── 3. Lock 으로 공유 자원 보호 ────

counter: int = 0          # 여러 스레드가 공유하는 카운터
lock: Lock = Lock()       # 동시 접근을 막는 뮤텍스 잠금


def increment(n: int) -> None:
    """counter 를 n 번 1씩 증가 (Lock 으로 보호)."""
    global counter
    for _ in range(n):
        with lock:          # 임계 구역 진입 시 lock 획득, 종료 시 자동 해제
            counter += 1


# ──── 4. 직렬 vs 병렬 비교 ────

def compare_serial_vs_parallel() -> None:
    """두 0.5초 작업을 직렬/병렬로 실행하고 경과 시간을 비교한다."""
    # 직렬 실행: 순서대로 호출
    t0 = time.time()
    sleep_worker("직렬-A", 0.5)
    sleep_worker("직렬-B", 0.5)
    serial_elapsed = time.time() - t0
    print(f"  직렬 실행 시간: {serial_elapsed:.2f}s")

    # 병렬 실행: Thread 2개를 동시에 시작
    t0 = time.time()
    t1 = Thread(target=sleep_worker, args=("병렬-A", 0.5))  # 스레드 생성
    t2 = Thread(target=sleep_worker, args=("병렬-B", 0.5))
    t1.start()   # 스레드 시작
    t2.start()
    t1.join()    # 메인 스레드가 t1 완료를 기다림
    t2.join()
    parallel_elapsed = time.time() - t0
    print(f"  병렬 실행 시간: {parallel_elapsed:.2f}s")
    print(f"  → 병렬이 약 {serial_elapsed / parallel_elapsed:.1f}배 빠름")


if __name__ == "__main__":
    print("=== 1. 직렬 vs 병렬 (IO-bound sleep) ===")
    compare_serial_vs_parallel()

    print("\n=== 2. Lock 으로 공유 카운터 보호 ===")
    counter = 0  # 초기화
    threads = [Thread(target=increment, args=(1000,)) for _ in range(5)]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    print(f"  최종 counter = {counter}  (기대: 5000)")
    assert counter == 5000, "Lock 없이 실행하면 경쟁 조건으로 값이 틀릴 수 있음"
    print("  Lock 보호 정상 동작 확인!")
