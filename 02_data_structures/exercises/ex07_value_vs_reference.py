"""
연습문제 07: 값 타입 / 참조 타입 / 가변 기본 인자.

4개 TODO 를 채워 모든 assert 를 통과하고 'OK' 가 출력되게 만드세요.
정답은 `solutions/ex07_value_vs_reference.py`.
"""

# ──── TODO 1: 같은 객체 공유 ────
# a 와 같은 객체를 가리키는 또 다른 이름 b 를 만드세요.
a = [1, 2, 3]
b = None  # ← 여기 채우기

b.append(4)
assert a is b, "b 가 a 와 같은 객체를 가리키지 않습니다"
assert a == [1, 2, 3, 4], "참조 공유라면 a 에도 변형이 보여야 합니다"


# ──── TODO 2: is 와 == 의 차이 ────
# 값은 같지만 정체성이 다른 두 리스트를 만드세요.
x = [1, 2, 3]
y = None  # ← 여기 채우기 (x 와 값은 같지만 별개 객체)

assert x == y, "값은 같아야 합니다"
assert x is not y, "별개 객체여야 합니다 (y = x 로 쓰면 안 됩니다)"


# ──── TODO 3: 함수 인자 — 재대입은 호출자에 보이지 않는다 ────
# 함수 안에서 lst 를 **재대입**만 하고 호출자의 원본은 건드리지 않도록 만드세요.

def rebind_only(lst):
    # TODO: lst 에 값을 더한 새 리스트를 만들어 lst 에 재대입하세요.
    #       힌트: lst = lst + [...] 또는 lst = [...] + lst
    pass


data = [1, 2, 3]
rebind_only(data)
assert data == [1, 2, 3], "재대입은 호출자에 보이지 않아야 합니다"


# ──── TODO 4: 가변 기본 인자 함정 회피 ────
# 호출할 때마다 새로운 빈 리스트로 시작하는 안전한 누적 함수를 만드세요.

def safe_append(item, bucket=...):   # TODO: 기본값을 None 으로 바꾸고 본문에서 처리
    # TODO: bucket 이 None 이면 새 빈 리스트로 시작, 그 후 item 추가하고 반환
    return None


assert safe_append(1) == [1]
assert safe_append(2) == [2], "호출 간에 리스트가 누적되면 안 됩니다"


print("OK")
