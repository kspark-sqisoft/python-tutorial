"""
연습문제 02 — else / finally 구조

safe_divide(a, b) 함수를 완성하세요.
- 정상적으로 나눌 수 있으면 결과(float)를 반환합니다.
- b 가 0 이면 None 을 반환합니다.
- 어느 경우든 finally 절에서 log["cleaned"] 를 True 로 설정해야 합니다.
"""

log = {"cleaned": False}


def safe_divide(a, b):
    # TODO: try / except / else / finally 를 모두 사용해 구현하세요
    pass


# ── 검증 ──
# 정상 나눗셈
log["cleaned"] = False
result = safe_divide(10, 2)
assert result == 5.0, f"예상 5.0, 실제 {result}"
assert log["cleaned"] is True, "finally 가 실행되지 않았습니다 (cleaned=False)"

# 0 으로 나누기
log["cleaned"] = False
result2 = safe_divide(10, 0)
assert result2 is None, f"예상 None, 실제 {result2}"
assert log["cleaned"] is True, "finally 가 실행되지 않았습니다 (cleaned=False)"

print("OK")
