"""
tuple — 파이썬의 불변(immutable) 순서 시퀀스.
list와 달리 생성 후 요소를 변경·추가·삭제할 수 없다.
Java의 final 배열, 또는 Scala의 불변 컬렉션과 유사한 철학.
함수 다중 반환값·딕셔너리 키·레코드 표현에 자주 쓰인다.
"""

# ──── 1. 튜플 생성 ────

empty = ()                   # 빈 튜플
triple = (1, 2, 3)           # 괄호 있는 튜플
bare = 1, 2, 3               # 괄호 없이도 튜플 (패킹)
from_list = tuple([4, 5, 6]) # list → tuple 변환
single = (42,)               # 단일 요소: 반드시 쉼표 필요
not_tuple = (42)             # 이건 그냥 정수 42 (괄호는 연산 우선순위용)

# ──── 2. 인덱싱·슬라이싱 ────

coords = (10, 20, 30)

x = coords[0]       # 첫 요소 → 10
z = coords[-1]      # 마지막 요소 → 30
xy = coords[:2]     # 앞 두 요소 슬라이싱 → (10, 20)

# ──── 3. 불변성 — 메서드는 count·index 뿐 ────

t = (1, 2, 2, 3, 2)

cnt = t.count(2)    # 값 2의 등장 횟수 → 3
idx = t.index(3)    # 값 3의 첫 번째 인덱스 → 3

# t[0] = 99         # TypeError: 튜플은 변경 불가

# ──── 4. 언패킹 ────

point = (3, 7)
px, py = point           # 각 요소를 별도 변수에 할당

rgb = (255, 128, 0)
r, g, b = rgb            # 3개 동시 언패킹

# 별표(*)로 나머지 모으기
first, *rest = (1, 2, 3, 4, 5)   # first=1, rest=[2,3,4,5]
*init, last = (1, 2, 3, 4, 5)    # init=[1,2,3,4], last=5
head, *mid, tail = (1, 2, 3, 4, 5)  # head=1, mid=[2,3,4], tail=5

# ──── 5. 함수 다중 반환 ────

def min_max(lst):
    """리스트의 최솟값과 최댓값을 동시에 반환."""
    return min(lst), max(lst)  # 튜플로 자동 패킹

lo, hi = min_max([4, 1, 7, 2, 9])  # 언패킹으로 바로 받기

# ──── 6. divmod — 내장 다중 반환 예시 ────

quotient, remainder = divmod(17, 5)  # 17 ÷ 5 의 몫과 나머지

# ──── 7. 튜플을 딕셔너리 키로 ────

# 리스트는 해시 불가 → 딕셔너리 키 사용 불가
# 튜플은 불변이므로 해시 가능 → 키로 사용 가능
distances = {
    (0, 0): 0,
    (3, 4): 5,   # 피타고라스 거리
}

dist = distances[(3, 4)]   # → 5

# ──── 8. 리스트 vs 튜플 선택 기준 ────

# 튜플: 고정된 이종(heterogeneous) 레코드 → (이름, 나이, 점수)
# 리스트: 동질(homogeneous) 요소의 컬렉션 → [점수1, 점수2, ...]


if __name__ == "__main__":
    # 데모 1: divmod로 다중 반환 받기
    n = 100
    for divisor in [3, 7, 11]:
        q, r = divmod(n, divisor)
        print(f"{n} ÷ {divisor} = 몫 {q}, 나머지 {r}")

    print()

    # 데모 2: 좌표 점 다루기
    points = [(1, 5), (3, 2), (7, 8), (2, 4)]
    sorted_points = sorted(points, key=lambda p: p[1])  # y 좌표 기준 정렬
    print("y 오름차순 정렬:", sorted_points)

    # 언패킹으로 좌표 꺼내기
    for px, py in sorted_points:
        print(f"  x={px}, y={py}")
