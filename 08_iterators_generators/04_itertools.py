"""
itertools 모듈 — 이터레이터를 다루는 표준 라이브러리 도구 모음.
무한 이터레이터(count/cycle/repeat), 연결(chain), 슬라이스(islice),
그룹화(groupby), 조합론(combinations/permutations)을 다룬다.
"""

import itertools

# ──── 1. 무한 이터레이터 ────

# count(start, step): start 부터 step 씩 증가하는 무한 수열
# islice 로 앞 5개만 잘라 무한 루프를 방지한다
evens = list(itertools.islice(itertools.count(0, 2), 5))
print("count(0, 2) 앞 5개:", evens)  # [0, 2, 4, 6, 8]

# cycle(seq): seq 를 무한 반복
# abc → a b c a b c a …
cycle_5 = list(itertools.islice(itertools.cycle("abc"), 7))
print("cycle('abc') 앞 7개:", cycle_5)

# repeat(x, times): x 를 times 번 반복 (times 생략 시 무한)
repeated = list(itertools.repeat("파이썬", 3))
print("repeat('파이썬', 3):", repeated)

# ──── 2. chain — 이터러블 연결 ────

# 여러 이터러블을 하나로 이어 붙인다
combined = list(itertools.chain([1, 2], [3, 4], [5]))
print("\nchain([1,2],[3,4],[5]):", combined)

# chain.from_iterable: 이중 리스트를 평탄화
nested = [[10, 20], [30, 40], [50]]
flat = list(itertools.chain.from_iterable(nested))
print("chain.from_iterable:", flat)

# ──── 3. islice — 이터레이터에서 일부만 잘라내기 ────

# islice(iter, stop) 또는 islice(iter, start, stop, step)
data = itertools.count(100)          # 100, 101, 102, …
sliced = list(itertools.islice(data, 3, 8))   # 인덱스 3~7
print("\nislice(count(100), 3, 8):", sliced)

# ──── 4. groupby — 연속된 동일 키 그룹화 ────

# ⚠ groupby 는 정렬된 데이터에서만 올바르게 동작한다
# 정렬하지 않으면 같은 키가 분리된 그룹으로 나타난다
words = ["apple", "ant", "banana", "bear", "cherry"]
words_sorted = sorted(words, key=lambda w: w[0])  # 첫 글자로 정렬

print("\ngroupby (첫 글자 기준):")
for key, group in itertools.groupby(words_sorted, key=lambda w: w[0]):
    print(f"  '{key}': {list(group)}")

# ──── 5. 조합론 — combinations / permutations ────

items = ["A", "B", "C"]

# combinations: 순서 없이 r 개 선택
combos = list(itertools.combinations(items, 2))
print("\ncombinations('ABC', 2):", combos)

# permutations: 순서 있게 r 개 선택
perms = list(itertools.permutations(items, 2))
print("permutations('ABC', 2):", perms)


if __name__ == "__main__":
    print("\n=== 데모 ===")

    # chain 예제
    print("chain([1,2],[3,4]):", list(itertools.chain([1, 2], [3, 4])))

    # islice + count 예제
    print("islice(count(0,2), 5):", list(itertools.islice(itertools.count(0, 2), 5)))

    # groupby 예제
    nums = sorted([1, 1, 2, 3, 3, 3, 4], )
    print("groupby 숫자 그룹:")
    for k, grp in itertools.groupby(nums):
        print(f"  {k}: {list(grp)}")
