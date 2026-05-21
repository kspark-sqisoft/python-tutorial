"""
연습문제 02 — Suppress 컨텍스트 매니저
지정한 예외 타입을 조용히 무시하는 클래스 기반 컨텍스트 매니저를 작성하라.
"""

# ──── TODO ────
# Suppress 클래스를 작성하라.
# - __init__(self, exc_type): 무시할 예외 타입을 저장한다.
# - __enter__(self): self 를 반환한다.
# - __exit__(self, exc_type, exc_val, exc_tb):
#     발생한 예외가 저장된 타입과 일치하면 True 를 반환하여 예외를 삼킨다.
#     다른 예외(또는 예외 없음)는 False(또는 None)를 반환하여 그대로 전파한다.

class Suppress:
    # TODO: 여기에 구현
    raise NotImplementedError


# ──── 검증 ────

# 케이스 1: 지정한 예외 → 무시되어야 한다
with Suppress(ValueError):
    int("abc")   # ValueError 발생 → 무시

# 케이스 2: 지정한 예외(KeyError) → 무시되어야 한다
with Suppress(KeyError):
    {}["없는키"]   # KeyError 발생 → 무시

# 케이스 3: 다른 예외 → 전파되어야 한다
try:
    with Suppress(KeyError):
        int("abc")   # ValueError 발생 → KeyError 가 아니므로 전파
    assert False, "ValueError 가 전파되지 않음"
except ValueError:
    pass   # 예상대로 ValueError 가 전파됨

# 케이스 4: 예외 없음 → 정상 통과
with Suppress(ValueError):
    x = 1 + 1   # 예외 없음 → 그냥 통과
assert x == 2

print("OK")
