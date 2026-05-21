"""
연습문제 01 — timing 데코레이터
함수를 감싸 실행 시간(초)을 딕셔너리 call_log 에 저장하는 데코레이터를 작성하라.
"""

import time

call_log = {}   # 함수 이름 → 마지막 실행 시간(초)

# ──── TODO ────
# timing(fn) 데코레이터를 작성하라.
# - fn 을 감싸는 wrapper 를 반환한다.
# - wrapper 는 fn 을 호출하기 전/후 시각을 측정하여
#   call_log[fn.__name__] 에 경과 시간(float, 초)을 저장한다.
# - fn 의 반환값을 그대로 돌려준다.
# - functools.wraps 를 사용하여 원본 함수 메타데이터를 보존한다.

def timing(fn):
    # TODO: 여기에 구현
    raise NotImplementedError


# ──── 검증 ────

@timing
def slow():
    """0.01초 이상 걸리는 함수."""
    time.sleep(0.01)

@timing
def fast(x):
    """즉시 반환하는 함수."""
    return x * 2

slow()
assert "slow" in call_log, "call_log 에 'slow' 키가 없음"
assert call_log["slow"] >= 0.01, "실행 시간이 0.01초 미만"

val = fast(21)
assert val == 42, "fast(21) 의 반환값이 42 가 아님"
assert "fast" in call_log, "call_log 에 'fast' 키가 없음"

import functools
assert slow.__name__ == "slow", "functools.wraps 미사용 — __name__ 이 'slow' 가 아님"

print("OK")
