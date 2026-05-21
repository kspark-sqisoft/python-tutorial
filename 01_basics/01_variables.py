"""
변수와 동적 타이핑 (Dynamic Typing)

Python 변수는 '이름표(label)'이다 — 객체 자체가 아닌 객체를 가리키는 참조.
C/Java처럼 타입을 선언하지 않으며, 재대입 시 타입이 바뀐다.
같은 객체를 여러 이름이 동시에 가리킬 수 있고, del 로 이름표만 떼어낼 수 있다.
"""

# ──── 1. 기본 대입 ────

x = 42          # 정수 객체 42 를 x 라는 이름표로 가리킴
name = "Alice"  # 문자열 객체를 name 으로 가리킴
pi = 3.14       # float 객체

# type() 로 현재 타입 확인
print(type(x))     # <class 'int'>
print(type(name))  # <class 'str'>
print(type(pi))    # <class 'float'>

# ──── 2. 동적 타이핑 — 재대입 시 타입 변경 ────

x = "이제 문자열"   # x 가 가리키는 객체 자체가 바뀜 (int → str)
print(type(x))      # <class 'str'>

# ──── 3. id() — 같은 객체를 두 이름이 가리키기 ────

a = [1, 2, 3]   # 리스트 객체 생성
b = a            # b 도 같은 리스트를 가리킴 (복사가 아님!)

print(id(a) == id(b))  # True — 동일한 객체
print(a is b)          # True — is 는 id 가 같은지 확인

# 작은 정수는 Python 내부에서 캐시(재사용)됨
m = 256
n = 256
print(m is n)   # True  (캐시 범위: -5 ~ 256)

# ──── 4. del — 이름표 떼기 ────

temp = "잠깐만 쓸 값"
print(temp)
del temp        # 이름표만 제거; 객체는 GC 가 회수
# print(temp)   # NameError 발생 — 이름표가 없으므로

# ──── 5. 튜플 언패킹 ────

x, y = 1, 2          # 오른쪽이 튜플 (1, 2) 로 묶여 풀림
print(x, y)          # 1 2

# 두 변수 교환 — 임시 변수 불필요
x, y = y, x
print(x, y)          # 2 1

first, *rest = [10, 20, 30, 40]  # 별표로 나머지 묶기
print(first, rest)               # 10 [20, 30, 40]

# ──── 6. 체인 대입 ────

a = b = c = 0        # 세 이름 모두 같은 0 객체를 가리킴
print(a, b, c)       # 0 0 0
print(id(a) == id(b) == id(c))  # True


if __name__ == "__main__":
    print("\n=== 변수 데모 ===")
    count = 100
    label = "항목"
    ratio = 0.75
    flag = True

    print(f"count  : {count}  | type={type(count).__name__}  | id={id(count)}")
    print(f"label  : {label}  | type={type(label).__name__} | id={id(label)}")
    print(f"ratio  : {ratio}  | type={type(ratio).__name__}  | id={id(ratio)}")
    print(f"flag   : {flag}   | type={type(flag).__name__}  | id={id(flag)}")

    # 같은 객체를 두 이름이 가리키는 예
    alias = count
    print(f"\ncount is alias → {count is alias}  (id 동일: {id(count) == id(alias)})")
