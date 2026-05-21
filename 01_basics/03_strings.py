"""
문자열 (Strings)

Python 문자열은 유니코드 문자의 불변(immutable) 시퀀스다.
Java/C#처럼 char 타입이 따로 없고, 한 글자도 str 이다.
작은따옴표·큰따옴표·삼중따옴표가 동등하며, f-string 으로 강력한 포맷팅을 제공한다.
"""

# ──── 1. 따옴표 종류 ────

s1 = '작은따옴표'
s2 = "큰따옴표"
s3 = """삼중따옴표:
여러 줄을
그대로 담는다."""

print(s1, s2)
print(s3)

# ──── 2. f-string 포맷팅 ────

name  = "Kee"
score = 95.678
count = 7

print(f"이름: {name}")              # 기본 삽입
print(f"표현식: {2 ** 8}")          # 표현식도 가능
print(f"repr: {name!r}")            # repr() 적용 → 따옴표 포함
print(f"소수점: {score:.2f}")       # 소수 둘째 자리까지
print(f"오른쪽 정렬: {count:>5}")   # 5칸 오른쪽 정렬
print(f"왼쪽 정렬: {name:<10}|")    # 10칸 왼쪽 정렬
print(f"가운데 정렬: {name:^10}|")  # 10칸 가운데 정렬
print(f"0 채우기: {count:03}")      # 3칸, 빈 자리는 0

# ──── 3. 주요 메서드 ────

sentence = "  Hello, World!  "

print(sentence.strip())                  # 양쪽 공백 제거
print(sentence.strip().lower())          # 소문자
print(sentence.strip().upper())          # 대문자
print("a,b,c".split(","))               # ['a', 'b', 'c']
print(", ".join(["사과", "배", "포도"])) # 사과, 배, 포도
print("Hello".replace("l", "r"))        # Herro
print("Hello".startswith("He"))         # True
print("Hello".endswith("lo"))           # True
print("Hello World".find("World"))      # 6  (없으면 -1)
print("abcabc".count("a"))             # 2

# ──── 4. 인덱싱과 슬라이싱 ────

s = "Python"

print(s[0])      # 'P'  — 첫 번째 문자
print(s[-1])     # 'n'  — 마지막 문자
print(s[1:4])    # 'yth' — 인덱스 1 이상 4 미만
print(s[:3])     # 'Pyt' — 처음부터 3 미만
print(s[3:])     # 'hon' — 3 이상 끝까지
print(s[::-1])   # 'nohtyP' — 역순 (step=-1)
print(s[::2])    # 'Pto'    — 두 칸씩 건너뜀

# ──── 5. 문자열 불변성 ────
# s[0] = 'J'  → TypeError: 'str' object does not support item assignment
# 변경하려면 새 문자열을 만들어야 한다:
new_s = "J" + s[1:]
print(new_s)   # 'Jython'


if __name__ == "__main__":
    print("\n=== 문자열 데모 ===")

    greeting = "안녕하세요, Python 세계!"
    print(f"원본     : {greeting}")
    print(f"대문자   : {greeting.upper()}")
    print(f"길이     : {len(greeting)}")
    print(f"역순     : {greeting[::-1]}")
    print(f"'Python' 위치: {greeting.find('Python')}")
    print(f"단어 분리: {greeting.split()}")

    # f-string 정렬 시연
    print("\n상품 목록:")
    items = [("사과", 1200), ("바나나", 800), ("체리", 3500)]
    print(f"{'상품':<8} {'가격':>6}")
    print("-" * 15)
    for item, price in items:
        print(f"{item:<8} {price:>6,}원")
