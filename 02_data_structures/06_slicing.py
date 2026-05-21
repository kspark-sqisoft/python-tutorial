"""
슬라이싱(slicing) — seq[start:stop:step] 으로 부분 시퀀스를 추출하는 파이썬 고유 문법.
stop 인덱스는 포함되지 않는다(exclusive).
list·tuple·str·range·bytes 모두 동일한 슬라이싱 규칙을 따른다.
Java의 substring/subList, JavaScript의 slice와 유사하지만 step 인수가 추가된다.
"""

# ──── 1. 기본 슬라이싱 ────

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

part = lst[2:5]     # 인덱스 2 이상 5 미만 → [2, 3, 4]
head = lst[:3]      # 처음부터 3개 → [0, 1, 2]
tail = lst[7:]      # 인덱스 7부터 끝까지 → [7, 8, 9]
all_ = lst[:]       # 전체 얕은 복사 → 새 리스트

# ──── 2. step 인수 ────

every2 = lst[::2]       # 두 칸씩 → [0, 2, 4, 6, 8]
every3 = lst[1::3]      # 1부터 세 칸씩 → [1, 4, 7]
reverse = lst[::-1]     # 역순 전체 → [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
rev_part = lst[7:2:-1]  # 7부터 3까지 역순 → [7, 6, 5, 4, 3]

# ──── 3. 음수 인덱스 ────

last = lst[-1]          # 마지막 → 9
last3 = lst[-3:]        # 뒤에서 3개 → [7, 8, 9]
except_last = lst[:-1]  # 마지막 제외 → [0, 1, 2, 3, 4, 5, 6, 7, 8]
neg_step = lst[-1:-5:-1]  # 뒤에서 -1씩 → [9, 8, 7, 6]

# ──── 4. 튜플·문자열도 동일 규칙 ────

tup = (10, 20, 30, 40, 50)
tup_part = tup[1:4]   # (20, 30, 40)
tup_rev = tup[::-1]   # (50, 40, 30, 20, 10)

s = "Hello, Python!"
word = s[7:13]        # 'Python'
rev_str = s[::-1]     # '!nohtyP ,olleH'
upper_only = s[::2]   # 짝수 인덱스 문자만

# ──── 5. range 슬라이싱 ────

r = range(20)
r_part = r[5:15:2]     # range(5, 15, 2) — 새 range 반환
r_list = list(r_part)  # [5, 7, 9, 11, 13]

# ──── 6. 리스트 슬라이스 대입 (list만 가능) ────

a = [1, 2, 3, 4, 5]
a[1:3] = [20, 30]       # 인덱스 1~2를 교체 → [1, 20, 30, 4, 5]
a[1:3] = [99]           # 2개를 1개로 교체 → [1, 99, 4, 5]
a[1:1] = [10, 11]       # 삽입 (제거 없이) → [1, 10, 11, 99, 4, 5]
a[2:4] = []             # 해당 범위 삭제 → [1, 10, 4, 5]

# ──── 7. 슬라이싱 경계 초과는 에러 없음 ────

short = [1, 2, 3]
safe = short[1:100]   # 범위 초과해도 OK → [2, 3]
empty_result = short[5:10]  # 완전히 벗어나면 빈 리스트 → []


def is_palindrome(seq):
    """시퀀스가 회문(앞뒤가 같은)인지 슬라이싱으로 검사."""
    return seq == seq[::-1]


if __name__ == "__main__":
    lst = list(range(10))
    print("원본:", lst)
    print("lst[2:5]:", lst[2:5])
    print("lst[:3]:", lst[:3])
    print("lst[7:]:", lst[7:])
    print("lst[::2]:", lst[::2])
    print("lst[::-1]:", lst[::-1])
    print("lst[-3:]:", lst[-3:])
    print()

    # 문자열 슬라이싱
    words = ["racecar", "python", "level", "kayak", "hello"]
    print("회문 검사:")
    for w in words:
        result = "회문" if is_palindrome(w) else "아님"
        print(f"  {w!r}: {result}")

    print()

    # 슬라이스 대입
    data = [1, 2, 3, 4, 5]
    print("슬라이스 대입 전:", data)
    data[1:4] = [20, 30]
    print("data[1:4] = [20, 30] 후:", data)
