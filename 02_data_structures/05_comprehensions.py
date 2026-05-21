"""
컴프리헨션(comprehension) — 시퀀스·집합·딕셔너리를 한 줄로 생성하는 파이썬 고유 문법.
Java의 Stream.map/filter, JavaScript의 Array.map/filter와 유사하지만
더 간결하고 파이썬다운(Pythonic) 표현이다.
list/dict/set/generator 네 가지 형태가 있다.
"""

# ──── 1. 리스트 컴프리헨션 기본 ────

squares = [x * x for x in range(1, 6)]   # [1, 4, 9, 16, 25]
# 동일한 결과를 for문으로:
# result = []
# for x in range(1, 6):
#     result.append(x * x)

# ──── 2. 조건 필터링 ────

evens = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]
big_squares = [x*x for x in range(10) if x > 5]   # [36, 49, 64, 81]

# 조건 표현식(삼항)을 식(expression) 위치에도 사용 가능
labels = ["짝수" if x % 2 == 0 else "홀수" for x in range(5)]

# ──── 3. 중첩 컴프리헨션 ────

# 두 시퀀스의 카르테시안 곱
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
# [(1,'a'), (1,'b'), (2,'a'), (2,'b'), (3,'a'), (3,'b')]

# 2D 리스트 평탄화
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [elem for row in matrix for elem in row]   # [1,2,3,4,5,6,7,8,9]

# ──── 4. 딕셔너리 컴프리헨션 ────

# 키: 단어, 값: 단어 길이
words = ["python", "java", "go", "rust"]
word_lengths = {w: len(w) for w in words}   # {'python':6, 'java':4, ...}

# (키, 값) 쌍을 뒤집어 새 dict 만들기
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}   # {1:'a', 2:'b', 3:'c'}

# 조건 포함
long_words = {w: len(w) for w in words if len(w) >= 4}

# ──── 5. 집합 컴프리헨션 ────

unique_lens = {len(w) for w in words}   # 단어 길이의 집합 (중복 제거)

# ──── 6. 제너레이터 표현식 ────

# 대괄호 대신 소괄호 → 이터레이터(generator) 반환 (메모리 절약)
gen = (x * x for x in range(10))   # 값을 미리 생성하지 않음

# sum 같은 함수에 직접 넘기면 메모리 효율적
total = sum(x * x for x in range(1_000_000))   # 리스트 안 만들고 합산

# next()로 하나씩 꺼내기
gen2 = (x for x in range(3))
first = next(gen2)   # 0
second = next(gen2)  # 1

# ──── 7. 가독성 주의 ────

# 컴프리헨션이 복잡해지면 일반 for문이 더 명확
# 한 줄 80자 초과, 중첩 3단계 이상이면 for문 고려


def make_multiplication_table(n):
    """n x n 구구단 딕셔너리 반환."""
    return {(i, j): i * j for i in range(1, n + 1) for j in range(1, n + 1)}


if __name__ == "__main__":
    # 데모 1: 단어 길이 매핑 dict
    sentence = "the quick brown fox jumps over the lazy dog"
    word_list = sentence.split()
    length_map = {w: len(w) for w in set(word_list)}
    print("단어 길이 맵 (고유 단어):")
    for word, length in sorted(length_map.items()):
        print(f"  {word!r}: {length}자")

    print()

    # 데모 2: 구구단 일부
    table = make_multiplication_table(9)
    print("구구단 (3단, 4단):")
    for i in [3, 4]:
        row = [f"{i}×{j}={table[(i,j)]}" for j in range(1, 10)]
        print("  " + "  ".join(row))

    print()

    # 데모 3: 제너레이터로 합계
    n = 100
    result = sum(x * x for x in range(1, n + 1))
    print(f"1~{n} 제곱합: {result}")
