"""
풀이 05 — property 와 캡슐화

왜 이렇게 풀었나:
__init__ 에서 self.balance = balance 로 setter 를 경유해 초기화하면 검증 로직이
한 곳(__init__ 과 setter 두 군데)에 중복되지 않는다. setter 에서 음수를 거부함으로써
외부 코드가 어떤 경로로 값을 바꾸더라도 불변식(잔액 >= 0)이 항상 유지된다.
실제 값은 _balance 에 저장하고 property 를 통해서만 접근하는 것이 관용적인 Python 패턴이다.
"""


class Account:
    def __init__(self, balance):
        self.balance = balance  # setter 경유

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("잔액은 음수일 수 없습니다")
        self._balance = value


acc = Account(1000)
assert acc.balance == 1000
acc.balance = 500
assert acc.balance == 500
try:
    acc.balance = -1
    assert False, "ValueError 가 발생해야 합니다"
except ValueError:
    pass
print("OK")
