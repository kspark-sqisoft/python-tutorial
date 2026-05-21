"""
표준 입출력과 포맷팅 (Standard I/O & Formatting)

print() 는 sep/end 키워드로 구분자와 줄끝을 제어한다.
input() 은 항상 str 을 반환하므로 숫자가 필요하면 변환이 필요하다.
f-string 의 정렬·너비·정밀도 지정자는 C의 printf 와 유사하지만 더 직관적이다.
비대화 환경에서 input() 을 호출하면 프로그램이 멈추므로 데모에서는 사용하지 않는다.
"""

# ──── 1. print() 기본 ────

print("안녕")                     # 기본: 마지막에 줄바꿈
print("하나", "둘", "셋")         # 공백으로 구분
print("하나", "둘", "셋", sep="-") # 구분자 변경 → 하나-둘-셋
print("끝에 공백", end=" ")       # 줄바꿈 대신 공백
print("← 같은 줄")               # 이 출력이 바로 이어짐

# 여러 값을 한 줄로
print("a", "b", "c", sep=", ", end="\n\n")   # a, b, c + 빈 줄

# ──── 2. input() — 주석 예제 ────
# 실제 실행 시 아래처럼 사용한다 (비대화 환경에서는 호출하지 않는다):
#
#   name = input("이름을 입력하세요: ")   # 항상 str 반환
#   age  = int(input("나이: "))           # 숫자가 필요하면 변환 필요
#   print(f"안녕하세요, {name}! {age}살이군요.")

# ──── 3. f-string 정렬 지정자 ────
# {값:<너비}  왼쪽 정렬 (left)
# {값:>너비}  오른쪽 정렬 (right)
# {값:^너비}  가운데 정렬 (center)
# {값:0>너비} 0 으로 채우기
# {값:.nf}    소수 n 자리

name  = "Kee"
score = 95
pi    = 3.14159

print(f"{'왼쪽':<10}|")   # 왼쪽 정렬, 10칸
print(f"{'오른쪽':>10}|") # 오른쪽 정렬
print(f"{'가운데':^10}|") # 가운데 정렬
print(f"{7:0>5}")          # 00007
print(f"{pi:.3f}")         # 3.142

# ──── 4. 콤마 천 단위 구분 ────

big_num = 1_234_567    # 언더스코어로 가독성 향상 (Python 3.6+)
print(f"{big_num:,}")  # 1,234,567

# ──── 5. 다양한 포맷 지정자 조합 ────

print(f"{'이름':<6} {'점수':>5} {'판정':^6}")
print("-" * 20)
data = [("Alice", 92, "합격"), ("Bob", 45, "불합격"), ("Carol", 78, "합격")]
for n, s, result in data:
    print(f"{n:<6} {s:>5} {result:^6}")


if __name__ == "__main__":
    print("\n=== 출력 포맷팅 데모 ===")

    # print sep/end 옵션
    print("=== sep 옵션 ===")
    print(2024, 5, 21, sep="-")          # 날짜 형식
    print("A", "B", "C", sep=" | ")     # 구분자

    print("\n=== f-string 포맷 ===")
    items = [
        ("사과",   1_200,  3),
        ("바나나",   800, 12),
        ("체리",   3_500,  2),
    ]
    header = f"{'품목':<8} {'단가':>8} {'수량':>4} {'소계':>10}"
    print(header)
    print("-" * len(header))
    total = 0
    for item, price, qty in items:
        subtotal = price * qty
        total += subtotal
        print(f"{item:<8} {price:>8,} {qty:>4} {subtotal:>10,}")
    print("-" * len(header))
    print(f"{'합계':<8} {'':>8} {'':>4} {total:>10,}")
