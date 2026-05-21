"""
연습문제 04 — 예외 계층 파악

아래 error_names 딕셔너리를 채우세요.
각 키에 해당하는 코드를 실행했을 때 발생하는 예외의 __name__ 을 값으로 넣습니다.

예:
    "div_zero"  → 1/0          → "ZeroDivisionError"
    "key_miss"  → {}["x"]      → "KeyError"
    "idx_out"   → [][0]        → "IndexError"
    "int_fail"  → int("a")     → "ValueError"
    "attr_miss" → None.foo     → "AttributeError"
"""

# TODO: 빈 문자열 "" 을 올바른 예외 이름으로 채우세요
error_names = {
    "div_zero":  "",
    "key_miss":  "",
    "idx_out":   "",
    "int_fail":  "",
    "attr_miss": "",
}


# ── 검증 ──
def get_exception_name(fn):
    try:
        fn()
    except Exception as e:
        return type(e).__name__

cases = {
    "div_zero":  lambda: 1 / 0,
    "key_miss":  lambda: {}["x"],
    "idx_out":   lambda: [][0],
    "int_fail":  lambda: int("a"),
    "attr_miss": lambda: getattr(None, "foo"),
}

for key, fn in cases.items():
    actual = get_exception_name(fn)
    given = error_names[key]
    assert given == actual, (
        f"'{key}': 예상 '{actual}', 입력값 '{given}'"
    )

print("OK")
