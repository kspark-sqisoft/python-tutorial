"""
연습문제 03 — NonNegative 디스크립터
0 이상의 값만 허용하는 데이터 디스크립터를 작성하라.
"""

# ──── TODO ────
# NonNegative 클래스를 작성하라.
# - 데이터 디스크립터: __set_name__, __get__, __set__ 을 구현한다.
# - __set__ 에서 value < 0 이면 ValueError 를 발생시킨다.
# - 0 과 양수는 정상 저장한다.
# - 실제 값은 인스턴스의 private 속성(예: "_stock")에 저장한다.

class NonNegative:
    # TODO: 여기에 구현
    raise NotImplementedError


# ──── 검증 ────

class Item:
    stock = NonNegative()   # 재고 수량 — 음수 불가
    price = NonNegative()   # 가격 — 음수 불가

item = Item()

# 0 과 양수는 허용
item.stock = 0
assert item.stock == 0, "stock = 0 이 저장되지 않음"

item.stock = 50
assert item.stock == 50, "stock = 50 이 저장되지 않음"

item.price = 1000
assert item.price == 1000, "price = 1000 이 저장되지 않음"

# 음수는 ValueError
try:
    item.stock = -1
    assert False, "음수 대입 시 ValueError 가 발생하지 않음"
except ValueError:
    pass

try:
    item.price = -500
    assert False, "음수 가격 대입 시 ValueError 가 발생하지 않음"
except ValueError:
    pass

# 값이 변경되지 않았는지 확인
assert item.stock == 50, "ValueError 후 stock 값이 변경됨"

print("OK")
