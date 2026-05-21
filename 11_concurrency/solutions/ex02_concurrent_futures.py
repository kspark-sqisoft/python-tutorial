"""
정답: ThreadPoolExecutor.map 으로 5개 task 를 병렬 처리.

왜 이렇게 하는가:
  - executor.map(fn, iterable) 은 각 원소에 fn 을 적용하고
    결과를 입력 순서대로 반환하는 생성기를 돌려준다.
  - with 블록을 벗어날 때 자동으로 shutdown(wait=True) 가 호출되어
    모든 작업이 완료된 뒤에야 다음 줄로 진행된다.
  - 5개 × 0.2s 작업이 동시 실행되므로 총 시간은 ~0.2s.
"""

import time
from concurrent.futures import ThreadPoolExecutor


def task(i: int) -> int:
    import time as _time
    _time.sleep(0.2)
    return i * i


t0 = time.perf_counter()

with ThreadPoolExecutor() as executor:
    total = sum(executor.map(task, range(5)))

elapsed = time.perf_counter() - t0

assert total == 0 + 1 + 4 + 9 + 16, f"결과 오류: {total}"
assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s"
print("OK")
