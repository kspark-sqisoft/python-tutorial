"""연습: Thread 2개로 IO-bound 작업을 병렬 실행하고 시간을 측정한다."""

import time
from threading import Thread

completed: list[int] = []   # 완료된 워커 수를 추적


def worker() -> None:
    """0.3초 sleep 하는 작업자."""
    time.sleep(0.3)
    completed.append(1)   # 완료 기록


# TODO: Thread 2개를 만들어 worker 를 동시에 실행하고
#       두 스레드가 모두 끝날 때까지 기다린다.
#       (t1, t2 변수에 Thread 를 만들고 start / join 사용)

t0 = time.perf_counter()

# --- 여기에 코드 작성 ---
t1 = None
t2 = None
# ----------------------

elapsed = time.perf_counter() - t0

assert len(completed) == 2, f"스레드가 실행되지 않음: completed={completed}"
assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s (병렬이면 ~0.3s 여야 함)"
print("OK")
