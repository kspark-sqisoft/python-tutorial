"""
람다와 고차함수 (Lambda & Higher-Order Functions)
- lambda 는 이름 없는 한 줄 함수로, 간단한 콜백에 자주 쓰인다.
- sorted/max/min 의 key= 인자, map/filter 의 함수 인자가 대표 활용처다.
- 파이썬에서 함수는 1급 객체 — 변수에 담고, 인자로 넘기고, 반환값으로 쓸 수 있다.
- map/filter 보다 리스트 컴프리헨션이 보통 더 파이썬다운 표현으로 여겨진다.
"""

# ──── 1. lambda 기본 ────

square = lambda x: x * x          # 변수에 람다 저장
add = lambda x, y: x + y          # 매개변수 두 개

# 일반 def 와 동등 — 단, def 는 이름이 있고 여러 줄 가능
def square_def(x):
    return x * x


# ──── 2. sorted / max / min 의 key ────

words = ["banana", "apple", "kiwi", "strawberry", "fig"]

# 단어 길이 기준 정렬
by_length = sorted(words, key=lambda w: len(w))

# 알파벳 마지막 글자 기준 정렬
by_last = sorted(words, key=lambda w: w[-1])

# 최장 단어
longest = max(words, key=len)      # 내장 len 을 직접 전달해도 된다


# ──── 3. map / filter vs 컴프리헨션 ────

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: 각 요소에 함수 적용 → map 객체 (지연 평가)
squares_map = list(map(lambda x: x * x, nums))

# 컴프리헨션 버전 — 더 파이썬다운 표현
squares_comp = [x * x for x in nums]

# filter: 조건을 만족하는 요소만 → filter 객체 (지연 평가)
evens_filter = list(filter(lambda x: x % 2 == 0, nums))

# 컴프리헨션 버전
evens_comp = [x for x in nums if x % 2 == 0]


# ──── 4. 함수를 인자로 / 반환값으로 ────

def apply(func, value):
    """함수를 인자로 받아 value 에 적용한다 — 고차함수."""
    return func(value)


def make_multiplier(n):
    """n 배 하는 함수를 반환한다 — 함수가 반환값."""
    return lambda x: x * n


# ──── 5. Demo: 사람 리스트 정렬 ────

people = [
    {"name": "서연",   "age": 28},
    {"name": "민준",   "age": 22},
    {"name": "지수아", "age": 35},
    {"name": "현우",   "age": 19},
]


if __name__ == "__main__":
    # ── lambda 기본 ──
    print(square(5))          # 25
    print(add(3, 7))          # 10

    # ── sorted key ──
    print(by_length)          # 길이 순
    print(by_last)            # 마지막 글자 순
    print(longest)            # strawberry

    # ── map/filter vs 컴프리헨션 ──
    print(squares_map)
    print(squares_comp)       # 결과 동일
    print(evens_filter)
    print(evens_comp)         # 결과 동일

    # ── 고차함수 ──
    print(apply(square, 6))              # 36
    triple = make_multiplier(3)
    print(triple(7))                     # 21

    # ── 이름 길이 기준 정렬 ──
    by_name_len = sorted(people, key=lambda p: len(p["name"]))
    for p in by_name_len:
        print(f"{p['name']} ({len(p['name'])}글자)")
