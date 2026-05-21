"""
list — 파이썬의 가변(mutable) 순서 시퀀스.
Java의 ArrayList, JavaScript의 Array와 유사하지만
슬라이싱·다중 타입 혼용·음수 인덱스 등 파이썬 고유 기능이 풍부하다.
요소를 언제든 추가·삭제·변경할 수 있다는 점이 tuple과의 핵심 차이다.
"""

# ──── 1. 리스트 생성 ────

empty = []                        # 빈 리스트
nums = [1, 2, 3, 4, 5]           # 정수 리스트
mixed = [1, "둘", 3.0, True]     # 여러 타입 혼용 가능
from_range = list(range(5))      # [0, 1, 2, 3, 4]
from_str = list("abc")           # ['a', 'b', 'c']

# ──── 2. 인덱싱 ────

first = nums[0]     # 첫 번째 요소 → 1
last = nums[-1]     # 마지막 요소 (음수 인덱스) → 5
third = nums[2]     # 세 번째 요소 → 3

# ──── 3. 슬라이싱 ────

part = nums[1:4]    # 인덱스 1 이상 4 미만 → [2, 3, 4]
step = nums[::2]    # 두 칸씩 → [1, 3, 5]
rev = nums[::-1]    # 역순 → [5, 4, 3, 2, 1]

# ──── 4. 변경 메서드 ────

a = [3, 1, 4, 1, 5]

a.append(9)           # 끝에 요소 추가
a.extend([2, 6])      # 다른 리스트의 요소를 통째로 추가
a.insert(0, 0)        # 인덱스 0 위치에 0 삽입
a.remove(1)           # 첫 번째로 나오는 1 제거 (없으면 ValueError)
popped = a.pop()      # 마지막 요소를 꺼내고 반환
popped_idx = a.pop(1) # 인덱스 1 요소를 꺼내고 반환
a.sort()              # 오름차순 정렬 (원본 변경)
a.reverse()           # 순서 뒤집기 (원본 변경)
a.clear()             # 모든 요소 삭제

# ──── 5. 비파괴 함수 ────

b = [3, 1, 2]

sorted_b = sorted(b)          # 새 정렬 리스트 반환, b 그대로
rev_list = list(reversed(b))  # 뒤집힌 새 리스트 (reversed는 이터레이터)
combined = [1, 2] + [3, 4]    # 두 리스트 연결 → 새 리스트
repeated = [0] * 4             # [0, 0, 0, 0]

# ──── 6. 중첩 리스트 (2D) ────

matrix = [
    [1, 2, 3],   # 첫 번째 행
    [4, 5, 6],   # 두 번째 행
    [7, 8, 9],   # 세 번째 행
]

center = matrix[1][1]   # 행 인덱스 1, 열 인덱스 1 → 5

# ──── 7. 가변성 주의 — 복사 ────

original = [1, 2, 3]
alias = original        # 같은 객체를 가리킴 (복사 아님)
alias.append(4)
# original 도 [1, 2, 3, 4] 로 바뀜!

shallow = original[:]   # 슬라이스 복사 → 독립된 새 리스트
shallow2 = list(original)  # list() 로도 동일한 얕은 복사

# ──── 8. 유용한 내장 함수 ────

nums2 = [3, 1, 4, 1, 5, 9]

length = len(nums2)      # 요소 개수 → 6
total = sum(nums2)       # 합계
minimum = min(nums2)     # 최솟값
maximum = max(nums2)     # 최댓값
count_1 = nums2.count(1) # 값 1의 등장 횟수 → 2
idx_4 = nums2.index(4)   # 값 4의 첫 번째 인덱스 → 2


if __name__ == "__main__":
    # 데모: 점수 리스트 만들고 정렬·필터링
    scores = [85, 72, 91, 64, 88, 55, 76, 93]
    print("원본 점수:", scores)

    scores.sort(reverse=True)   # 내림차순 정렬
    print("정렬 후:", scores)

    # 80점 이상만 필터링 (컴프리헨션 미리 맛보기)
    passing = [s for s in scores if s >= 80]
    print("80점 이상:", passing)

    print("최고:", max(scores), "/ 최저:", min(scores), "/ 평균:", sum(scores) / len(scores))
