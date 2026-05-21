"""
정답 02 — Suppress 컨텍스트 매니저

핵심 아이디어:
  __exit__ 의 첫 번째 인자 exc_type 이 저장된 예외 타입과 일치하면
  True 를 반환하여 예외를 삼킨다.
  일치하지 않거나 예외가 없으면 False(None)를 반환하여 정상 흐름을 유지한다.

왜 issubclass 를 쓰는가?
  exc_type == self._exc_type 은 정확히 같은 타입만 잡는다.
  issubclass(exc_type, self._exc_type) 를 쓰면 서브클래스 예외도 함께 잡을 수 있어
  파이썬 표준 except 구문과 동일한 의미론을 갖는다.
"""


class Suppress:
    def __init__(self, exc_type):
        self._exc_type = exc_type   # 무시할 예외 타입 저장

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return False                                # 예외 없음 → 그냥 통과
        if issubclass(exc_type, self._exc_type):
            return True                                 # 지정 예외 → 삼킴
        return False                                    # 다른 예외 → 전파


# ──── 검증 ────

with Suppress(ValueError):
    int("abc")

with Suppress(KeyError):
    {}["없는키"]

try:
    with Suppress(KeyError):
        int("abc")
    assert False
except ValueError:
    pass

with Suppress(ValueError):
    x = 1 + 1
assert x == 2

print("OK")
