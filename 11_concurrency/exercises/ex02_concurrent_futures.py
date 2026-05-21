"""연습: ThreadPoolExecutor.map 으로 5개 작업을 병렬 처리하고 결과를 합산한다."""

import time
from concurrent.futures import ThreadPoolExecutor


def task(i: int) -> int:
    """0.2초 sleep 후 i*i 를 반환."""
    time.sleep(0.2)
    return i * i


# TODO: ThreadPoolExecutor 를 사용해 task 를 0~4 에 대해 병렬 실행하고
#       결과를 모두 합산해 total 에 저장한다.
#       (executor.map 사용 권장)

t0 = time.perf_counter()

# --- 여기에 코드 작성 ---
total = None
# ----------------------

elapsed = time.perf_counter() - t0

assert total == 0 + 1 + 4 + 9 + 16, f"결과 오류: {total}"
assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s (병렬이면 ~0.2s 여야 함)"
print("OK")
