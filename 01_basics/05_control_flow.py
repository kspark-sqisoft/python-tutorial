"""
제어흐름 (Control Flow)

Python 은 중괄호 대신 들여쓰기로 블록을 구분한다.
for 는 이터러블을 직접 순회하며, range/enumerate/zip 이 자주 쓰인다.
루프에 else 절을 붙일 수 있다 — break 없이 완료 시 실행된다.
match (Python 3.10+) 는 C의 switch 보다 표현력이 강한 구조적 패턴 매칭이다.
"""

# ──── 1. if / elif / else ────

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수 {score} → 등급 {grade}")   # C

# ──── 2. while — break / continue ────

n = 0
while n < 5:
    n += 1
    if n == 3:
        continue    # 3은 건너뜀
    print(n, end=" ")
print()   # 1 2 4 5

# break 로 조기 종료
count = 0
while True:          # 무한 루프
    count += 1
    if count >= 3:
        break        # 조건 충족 시 탈출
print(f"count = {count}")   # 3

# ──── 3. for — range / enumerate / zip ────

# range(시작, 끝, 간격)
for i in range(0, 10, 3):
    print(i, end=" ")   # 0 3 6 9
print()

# enumerate — 인덱스와 값을 동시에
fruits = ["사과", "배", "포도"]
for idx, fruit in enumerate(fruits, start=1):  # 1부터 시작
    print(f"{idx}. {fruit}")

# zip — 두 이터러블을 묶어 병렬 순회
names  = ["Alice", "Bob", "Carol"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ──── 4. 루프 else ────
# break 없이 루프가 끝났을 때만 else 블록이 실행된다

for i in range(5):
    if i == 10:       # 절대 True 가 되지 않음
        break
else:
    print("루프 else: break 없이 완료")   # 출력됨

for i in range(5):
    if i == 3:
        break         # break 발생
else:
    print("이 줄은 출력되지 않음")        # 출력 안 됨

# ──── 5. match (Python 3.10+) ────

def describe(value):
    match value:
        case 0:
            return "영"
        case 1 | 2:          # OR 패턴
            return "하나 또는 둘"
        case str():          # 타입 패턴
            return f"문자열: {value!r}"
        case _:              # 와일드카드 (default)
            return "그 외"

for v in [0, 1, 2, 3, "hello", 99]:
    print(f"match({v!r:10}) → {describe(v)}")


if __name__ == "__main__":
    print("\n=== FizzBuzz 1~15 ===")
    for i in range(1, 16):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()
