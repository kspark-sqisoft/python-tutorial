"""
디스크립터(Descriptor) 학습 모듈.
__get__ / __set__ / __delete__ 를 구현한 클래스가
다른 클래스의 속성 접근을 가로채는 원리를 다룬다.
"""

# ──── 1. 디스크립터란? ────

# 디스크립터 = __get__, __set__, __delete__ 중 하나 이상을 가진 클래스
# 어떤 클래스(소유 클래스)의 클래스 속성으로 두면,
# 인스턴스에서 그 속성에 접근할 때 파이썬이 디스크립터 메서드를 대신 호출한다
#
# @property 의 내부 구현이 바로 이 디스크립터 프로토콜이다


# ──── 2. 데이터 디스크립터 vs 비데이터 디스크립터 ────

# 데이터 디스크립터    : __set__ 또는 __delete__ 를 구현 → 인스턴스 __dict__ 보다 우선
# 비데이터 디스크립터 : __get__ 만 구현 → 인스턴스 __dict__ 에 같은 이름이 있으면 가려짐


# ──── 3. 검증용 디스크립터 예시 — Positive ────

class Positive:
    """양수만 허용하는 데이터 디스크립터."""

    def __set_name__(self, owner, name):
        # 파이썬 3.6+ — 소유 클래스에 붙을 때 자동 호출되어 속성 이름을 알 수 있다
        self._name = name               # 예: "amount"
        self._private = f"_{name}"     # 실제 값 저장용 키: "_amount"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                 # 클래스에서 접근 시 디스크립터 자체를 반환
        return getattr(obj, self._private, None)

    def __set__(self, obj, value):
        if value <= 0:                  # 양수가 아니면 거부
            raise ValueError(f"{self._name} 은(는) 양수여야 합니다. 받은 값: {value}")
        setattr(obj, self._private, value)  # 검증 통과 시 저장

    def __delete__(self, obj):
        delattr(obj, self._private)


class Order:
    """주문 금액과 수량에 Positive 디스크립터를 적용한 클래스."""
    amount = Positive()     # 클래스 속성으로 디스크립터 인스턴스를 둔다
    quantity = Positive()


# ──── 4. @property 와의 관계 ────

# @property 는 내부적으로 아래와 동일한 디스크립터를 만든다:
#
# class property:
#     def __init__(self, fget=None, fset=None, fdel=None): ...
#     def __get__(self, obj, objtype=None): ...
#     def __set__(self, obj, value): ...
#     def __delete__(self, obj): ...
#
# 즉 @property 는 편리한 디스크립터 문법 설탕(syntactic sugar)이다


# ──── 5. 읽기 전용 디스크립터 (비데이터 디스크립터) ────

class Constant:
    """항상 같은 값을 반환하는 읽기 전용 비데이터 디스크립터."""

    def __init__(self, value):
        self._value = value     # 반환할 고정 값

    def __get__(self, obj, objtype=None):
        return self._value      # __set__ 없음 → 비데이터 디스크립터


class Config:
    MAX_RETRIES = Constant(5)   # 클래스/인스턴스 어디서 읽어도 5


if __name__ == "__main__":
    # Positive 디스크립터 시연
    print("=== Positive 디스크립터 ===")
    o = Order()

    o.amount = 100          # 양수 → 정상
    o.quantity = 3
    print(f"amount={o.amount}, quantity={o.quantity}")

    try:
        o.amount = -1       # 음수 → ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        o.amount = 0        # 0 → ValueError
    except ValueError as e:
        print(f"ValueError: {e}")

    print()

    # Constant 디스크립터 시연
    print("=== Constant 디스크립터 ===")
    cfg = Config()
    print(f"Config.MAX_RETRIES = {Config.MAX_RETRIES}")
    print(f"cfg.MAX_RETRIES    = {cfg.MAX_RETRIES}")

    print()

    # @property 는 디스크립터다
    print("=== @property 는 디스크립터 ===")
    print(f"type(Order.__dict__['amount']) = {type(Order.__dict__['amount'])}")
    # → <class '__main__.Positive'>  (디스크립터 인스턴스임을 확인)
