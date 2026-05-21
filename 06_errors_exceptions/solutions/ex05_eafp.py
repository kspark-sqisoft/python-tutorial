"""
해설 — lookup_eafp

핵심 이유:
  EAFP 패턴: "먼저 물어보지 않고 시도하고, 실패하면 처리한다."
  key in d 를 먼저 확인(LBYL)하는 것보다 try/except KeyError 가 더 파이썬답다.
  특히 딕셔너리 접근이 빈번한 루프에서는 EAFP 가 불필요한 중복 탐색을 줄인다.
  d.get(key, default) 는 내부적으로 같은 논리지만,
  직접 try/except 를 쓰면 더 복잡한 연산에도 동일 패턴을 적용할 수 있다.
"""


def lookup_eafp(d, key, default=None):
    try:
        return d[key]
    except KeyError:
        return default


# ── 검증 ──
data = {"name": "Alice", "score": 95, "active": True}

assert lookup_eafp(data, "name") == "Alice"
assert lookup_eafp(data, "score") == 95
assert lookup_eafp(data, "active") is True

assert lookup_eafp(data, "age") is None
assert lookup_eafp(data, "age", 0) == 0
assert lookup_eafp(data, "missing", "기본값") == "기본값"

assert lookup_eafp({}, "x", 42) == 42

print("OK")
