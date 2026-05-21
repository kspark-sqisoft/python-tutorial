"""
정답 03 — NonNegative 디스크립터

핵심 아이디어:
  __set_name__ 으로 속성 이름을 알아낸 뒤,
  실제 값은 인스턴스의 "_속성명" private 키에 저장한다.
  __set__ 에서 음수를 거부함으로써 클래스 정의 시점이 아닌
  대입 시점에 검증이 이루어진다.

왜 private 키에 저장하는가?
  디스크립터 이름과 같은 키(예: "stock")에 저장하면
  __set__ 이 재귀적으로 호출되는 무한루프에 빠진다.
  "_stock" 처럼 다른 이름을 써서 충돌을 피한다.
"""


class NonNegative:
    def __set_name__(self, owner, name):
        self._name = name               # 공개 속성명 (예: "stock")
        self._private = f"_{name}"     # 저장용 private 키 (예: "_stock")

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                 # 클래스에서 접근 시 디스크립터 반환
        return getattr(obj, self._private, None)

    def __set__(self, obj, value):
        if value < 0:                   # 음수 거부
            raise ValueError(
                f"{self._name} 은(는) 0 이상이어야 합니다. 받은 값: {value}"
            )
        setattr(obj, self._private, value)


# ──── 검증 ────

class Item:
    stock = NonNegative()
    price = NonNegative()

item = Item()

item.stock = 0
assert item.stock == 0

item.stock = 50
assert item.stock == 50

item.price = 1000
assert item.price == 1000

try:
    item.stock = -1
    assert False
except ValueError:
    pass

try:
    item.price = -500
    assert False
except ValueError:
    pass

assert item.stock == 50

print("OK")
