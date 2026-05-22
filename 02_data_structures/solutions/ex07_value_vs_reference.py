"""
풀이 07: 값 / 참조 / 가변 기본 인자.

- `b = a` 는 복사가 아니라 같은 객체에 이름을 하나 더 붙이는 것뿐 — `a is b` 가 True 가 된다.
- 값이 같아도 별개 객체를 만들려면 새 리터럴(`[1, 2, 3]`)이나 명시적 복사(`a.copy()`)를 써야 한다.
- 함수 안에서 매개변수에 **재대입**하면 지역 이름만 바뀌어 호출자에는 영향이 없다.
- 가변 기본 인자는 함수 정의 시 한 번만 평가되므로, 안전한 관용구는 기본값을 `None` 으로 두고 본문에서 새로 만드는 것이다.
"""

# 1. 참조 공유
a = [1, 2, 3]
b = a                                # 같은 객체에 이름만 추가

b.append(4)
assert a is b
assert a == [1, 2, 3, 4]


# 2. is vs ==
x = [1, 2, 3]
y = [1, 2, 3]                        # 같은 값을 가진 새 리스트 — 별개 객체

assert x == y
assert x is not y


# 3. 재대입은 호출자에 보이지 않는다
def rebind_only(lst):
    lst = lst + [99]                 # 지역 이름 lst 만 다른 객체를 가리킴


data = [1, 2, 3]
rebind_only(data)
assert data == [1, 2, 3]


# 4. 가변 기본 인자 함정 회피
def safe_append(item, bucket=None):
    if bucket is None:
        bucket = []                  # 호출 시점마다 새 리스트
    bucket.append(item)
    return bucket


assert safe_append(1) == [1]
assert safe_append(2) == [2]


print("OK")
