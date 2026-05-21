"""
연습문제 05 — EAFP 패턴으로 dict 접근

lookup_eafp(d, key, default) 함수를 완성하세요.
- try/except KeyError 패턴을 사용해 dict d 에서 key 를 조회합니다.
- 키가 있으면 해당 값을 반환합니다.
- 키가 없으면 default 를 반환합니다.
- d.get() 을 사용하지 말고 try/except 로 구현하세요.
"""


def lookup_eafp(d, key, default=None):
    # TODO: try/except KeyError 를 사용해 구현하세요
    pass


# ── 검증 ──
data = {"name": "Alice", "score": 95, "active": True}

# 키가 있는 경우
assert lookup_eafp(data, "name") == "Alice"
assert lookup_eafp(data, "score") == 95
assert lookup_eafp(data, "active") is True

# 키가 없는 경우 — default 사용
assert lookup_eafp(data, "age") is None
assert lookup_eafp(data, "age", 0) == 0
assert lookup_eafp(data, "missing", "기본값") == "기본값"

# 빈 딕셔너리
assert lookup_eafp({}, "x", 42) == 42

print("OK")
