"""
정답 01 — timing 데코레이터

핵심 아이디어:
  time.perf_counter() 로 fn 호출 전후 시각을 재고,
  그 차이를 call_log[fn.__name__] 에 저장한다.
  functools.wraps 를 붙여 원본 __name__ / __doc__ 을 보존한다.

왜 perf_counter 인가?
  time.time() 보다 해상도가 높고 단조 증가(monotonic)하여
  짧은 구간 측정에 적합하다.
"""

import time
import functools

call_log = {}


def timing(fn):
    @functools.wraps(fn)                        # 원본 메타데이터 보존
    def wrapper(*args, **kwargs):
        start = time.perf_counter()             # 시작 시각
        result = fn(*args, **kwargs)            # 원본 함수 실행
        call_log[fn.__name__] = time.perf_counter() - start  # 경과 시간 저장
        return result                           # 반환값 그대로 전달
    return wrapper


# ──── 검증 ────

@timing
def slow():
    time.sleep(0.01)

@timing
def fast(x):
    return x * 2

slow()
assert "slow" in call_log
assert call_log["slow"] >= 0.01

val = fast(21)
assert val == 42
assert "fast" in call_log
assert slow.__name__ == "slow"

print("OK")
