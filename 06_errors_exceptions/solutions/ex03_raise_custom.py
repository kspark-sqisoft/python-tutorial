"""
해설 — NegativeError + must_be_positive

핵심 이유:
  Exception 을 상속하면 표준 예외 처리 흐름에 자연스럽게 통합된다.
  __init__ 에서 super().__init__(메시지) 를 호출해 str(e) 가 동작하게 하고,
  .value 같은 추가 속성을 저장하면 호출자가 예외 객체에서 세부 정보를 꺼낼 수 있다.
  raise 는 함수 계약(양수여야 한다)을 명시적으로 강제하는 수단이다.
"""


class NegativeError(Exception):
    """0 이하의 값이 전달됐을 때 발생하는 사용자 정의 예외."""

    def __init__(self, value):
        super().__init__(f"양수여야 합니다: {value}")
        self.value = value  # 호출자가 원래 값을 꺼낼 수 있도록


def must_be_positive(n):
    if n <= 0:
        raise NegativeError(n)
    return n


# ── 검증 ──
assert must_be_positive(5) == 5
assert must_be_positive(1) == 1

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
