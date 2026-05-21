"""
해설 — error_names 채우기

핵심 이유:
  각 표현식이 발생시키는 예외 이름을 외우는 것보다,
  실제로 실행해보고 type(e).__name__ 으로 확인하는 습관이 중요하다.
  예외 계층을 알면 except LookupError 처럼 부모로 묶어 처리할 수 있어
  코드가 간결해진다.
"""

error_names = {
    "div_zero":  "ZeroDivisionError",  # 1/0
    "key_miss":  "KeyError",           # {}["x"]
    "idx_out":   "IndexError",         # [][0]
    "int_fail":  "ValueError",         # int("a")
    "attr_miss": "AttributeError",     # None.foo
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
