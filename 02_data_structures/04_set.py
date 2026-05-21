"""
set — 파이썬의 집합(set) 자료구조.
Java의 HashSet, 수학의 집합과 동일한 개념.
중복을 허용하지 않으며, 순서가 없다(unordered).
원소 존재 여부 검사가 O(1) 이므로 list보다 훨씬 빠르다.
"""

# ──── 1. 집합 생성 ────

empty = set()              # 빈 집합 ({}는 빈 dict이므로 set() 사용!)
nums = {1, 2, 3, 4, 5}    # 중괄호로 직접 생성
from_list = set([1, 2, 2, 3, 3, 3])  # 중복 자동 제거 → {1, 2, 3}
from_str = set("banana")   # {'b', 'a', 'n'} (중복 제거, 순서 없음)

# ──── 2. 요소 추가·제거 ────

s = {1, 2, 3}

s.add(4)          # 요소 추가 (이미 있으면 무시)
s.add(2)          # 이미 있으므로 변화 없음
s.discard(10)     # 없어도 에러 없이 무시 (안전한 삭제)
s.remove(1)       # 있으면 삭제, 없으면 KeyError
val = s.pop()     # 임의의 요소 하나 꺼내고 반환 (순서 없음)

# ──── 3. 집합 연산 ────

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

intersection = a & b        # 교집합: 양쪽 모두에 있는 요소 → {3, 4}
union = a | b               # 합집합: 둘 중 하나라도 있는 요소 → {1,2,3,4,5,6}
difference = a - b          # 차집합: a에만 있는 요소 → {1, 2}
sym_diff = a ^ b            # 대칭차집합: 한쪽에만 있는 요소 → {1,2,5,6}

# 메서드로도 동일하게 수행 가능
same_inter = a.intersection(b)
same_union = a.union(b)
same_diff = a.difference(b)

# ──── 4. 집합 관계 검사 ────

small = {1, 2}
big = {1, 2, 3, 4}

is_subset = small <= big         # 부분집합 여부 → True
is_superset = big >= small       # 상위집합 여부 → True
is_disjoint = small.isdisjoint({5, 6})  # 공통 원소 없음 → True

# ──── 5. in 검사 O(1) ────

large_list = list(range(10_000))
large_set = set(large_list)

# list 검사: O(n) — 최악의 경우 전체 순회
found_list = 9_999 in large_list   # 느림

# set 검사: O(1) — 해시 테이블
found_set = 9_999 in large_set     # 빠름

# ──── 6. frozenset — 불변 집합 ────

fs = frozenset([1, 2, 3])   # 한 번 만들면 변경 불가
# fs.add(4)                 # AttributeError: frozenset은 add 없음
# 딕셔너리 키나 집합의 원소로 사용 가능 (hashable)


def common_elements(lst1, lst2):
    """두 리스트의 공통 원소를 집합으로 반환."""
    return set(lst1) & set(lst2)


if __name__ == "__main__":
    # 데모: 두 리스트의 공통 원소 찾기
    users_a = ["철수", "영희", "민준", "서연", "지호"]
    users_b = ["영희", "지호", "하준", "지아", "철수"]

    common = common_elements(users_a, users_b)
    only_a = set(users_a) - set(users_b)
    only_b = set(users_b) - set(users_a)

    print("공통 사용자:", common)
    print("A에만 있는 사용자:", only_a)
    print("B에만 있는 사용자:", only_b)
    print("전체 사용자 수:", len(set(users_a) | set(users_b)))

    # 중복 제거 예시
    tags = ["파이썬", "코딩", "파이썬", "데이터", "코딩", "파이썬"]
    unique_tags = sorted(set(tags))  # 중복 제거 후 정렬
    print("\n고유 태그:", unique_tags)
