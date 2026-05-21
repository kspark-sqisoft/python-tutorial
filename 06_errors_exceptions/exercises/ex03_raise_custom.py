"""
연습문제 03 — 사용자 정의 예외

1. NegativeError(Exception) 클래스를 정의하세요.
   - 생성자에서 전달받은 숫자를 포함하는 메시지를 설정합니다.
   - .value 속성으로 원래 숫자를 꺼낼 수 있어야 합니다.

2. must_be_positive(n) 함수를 완성하세요.
   - n 이 0 이하면 NegativeError 를 raise 합니다.
   - 양수면 n 을 그대로 반환합니다.
"""


# TODO: NegativeError 클래스 정의
class NegativeError(Exception):
    pass


def must_be_positive(n):
    # TODO: 구현하세요
    pass


# ── 검증 ──
# 정상 케이스
assert must_be_positive(5) == 5
assert must_be_positive(1) == 1

# 예외 케이스
try:
    must_be_positive(-3)
    assert False, "NegativeError 가 발생해야 합니다"
except NegativeError as e:
    assert e.value == -3, f"예상 e.value=-3, 실제 {e.value}"

try:
    must_be_positive(0)
    assert False, "NegativeError 가 발생해야 합니다"
except NegativeError as e:
    assert e.value == 0, f"예상 e.value=0, 실제 {e.value}"

print("OK")
