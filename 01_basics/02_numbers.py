"""
숫자와 연산자 (Numbers & Operators)

Python int 는 임의 정밀도(arbitrary precision) — 크기 제한이 없다.
C/Java의 int(32비트 고정)와 달리 오버플로우가 발생하지 않는다.
float 는 IEEE 754 배정밀도(64비트), complex 는 실수+허수 쌍으로 내장 지원.
"""

# ──── 1. 정수 (int) — 임의 정밀도 ────

small = 42
big = 2 ** 100          # 10진수 30자리가 넘는 수도 정확히 표현
print(small)            # 42
print(big)              # 1267650600228229401496703205376
print(type(big))        # <class 'int'>

# ──── 2. 실수 (float) ────

f = 3.14
g = 1.5e3               # 1500.0 (과학적 표기법)
print(f, g)             # 3.14 1500.0
print(type(f))          # <class 'float'>

# ──── 3. 복소수 (complex) — 간단히 ────

c = 2 + 3j              # j 를 허수 단위로 사용 (수학 i)
print(c)                # (2+3j)
print(c.real, c.imag)   # 2.0 3.0

# ──── 4. 사칙연산과 특수 연산자 ────

a, b = 17, 5

print(a + b)    # 22  — 덧셈
print(a - b)    # 12  — 뺄셈
print(a * b)    # 85  — 곱셈
print(a / b)    # 3.4 — 나눗셈 (항상 float 반환)
print(a ** b)   # 1419857 — 거듭제곱 (pow(a, b) 와 동일)
print(a // b)   # 3  — 정수 나눗셈 (floor division)
print(a % b)    # 2  — 나머지

# ──── 5. divmod() — 몫과 나머지를 한 번에 ────

q, r = divmod(a, b)
print(f"{a} ÷ {b} = {q} 나머지 {r}")   # 17 ÷ 5 = 3 나머지 2

# ──── 6. 타입 변환과 내장 함수 ────

print(int(3.9))     # 3    — 소수점 아래 버림 (반올림 아님)
print(float(7))     # 7.0
print(round(3.567, 2))   # 3.57
print(round(2.5))        # 2   — 반올림 (Python 은 banker's rounding: 짝수 쪽으로)
print(abs(-42))          # 42

# ──── 7. 진법 표기 ────

binary = 0b1010     # 2진수 → 10
octal  = 0o17       # 8진수 → 15
hexa   = 0xFF       # 16진수 → 255

print(binary, octal, hexa)        # 10 15 255
print(bin(255), oct(255), hex(255))  # 0b11111111 0o377 0xff


if __name__ == "__main__":
    print("\n=== 숫자 데모 ===")

    # 임의 정밀도 시연
    result = 2 ** 100
    print(f"2 ** 100 = {result}")
    print(f"자릿수: {len(str(result))}자리")

    # 연산자 요약 표
    print("\n연산자 요약 (a=17, b=5)")
    ops = [
        ("a + b",  a + b,  "덧셈"),
        ("a - b",  a - b,  "뺄셈"),
        ("a * b",  a * b,  "곱셈"),
        ("a / b",  a / b,  "나눗셈(float)"),
        ("a ** b", a ** b, "거듭제곱"),
        ("a // b", a // b, "정수나눗셈"),
        ("a % b",  a % b,  "나머지"),
    ]
    for expr, val, desc in ops:
        print(f"  {expr:<8} = {str(val):<12} # {desc}")
