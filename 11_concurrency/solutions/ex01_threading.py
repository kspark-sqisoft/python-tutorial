"""
정답: Thread 2개로 0.3초 작업을 병렬 실행.

왜 이렇게 하는가:
  - Thread(target=fn) 으로 스레드를 생성만 하고 start() 로 실행을 시작한다.
  - join() 은 해당 스레드가 끝날 때까지 메인 스레드를 대기시킨다.
  - 두 스레드가 동시에 sleep 하므로 총 시간은 ~0.3s (직렬이면 ~0.6s).
  - IO-bound 작업에서 GIL 이 sleep 중 해제되므로 진짜 병렬처럼 동작한다.
"""

import time
from threading import Thread


def worker() -> None:
    time.sleep(0.3)


t0 = time.perf_counter()

t1 = Thread(target=worker)
t2 = Thread(target=worker)
t1.start()
t2.start()
t1.join()
t2.join()

elapsed = time.perf_counter() - t0

assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s"
print("OK")
