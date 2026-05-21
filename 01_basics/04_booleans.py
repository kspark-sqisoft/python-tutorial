"""
불리언과 truthy/falsy (Booleans & Truthiness)

Python 의 True/False 는 첫 글자가 대문자 — JavaScript의 true/false 와 다르다.
bool 은 int 의 서브클래스이므로 True==1, False==0 이 성립한다.
'falsy' 값(0, "", [], None 등)은 조건문에서 False 처럼 동작한다.
and/or 는 단락 평가(short-circuit)로 bool 이 아닌 값 자체를 반환한다.
"""

# ──── 1. True / False 기본 ────

t = True
f = False

print(type(t))       # <class 'bool'>
print(isinstance(t, int))   # True — bool 은 int 의 서브클래스
print(True + True)   # 2  (True=1, False=0 으로 연산 가능)

# ──── 2. 비교 연산자 ────

x = 5

print(x == 5)    # True  — 값이 같은가
print(x != 3)    # True  — 값이 다른가
print(x < 10)    # True
print(x >= 5)    # True

# ──── 3. == vs is ────

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  — 값(내용)이 같음
print(a is b)    # False — 서로 다른 객체
print(a is c)    # True  — 같은 객체를 가리킴

# None 비교는 is 를 사용하는 것이 관례
val = None
print(val is None)   # True  (val == None 보다 권장)

# ──── 4. in / not in ────

fruits = ["사과", "배", "포도"]
print("사과" in fruits)      # True
print("바나나" not in fruits) # True

# ──── 5. truthy / falsy ────
# False 로 평가되는 값들:
# False, None, 0, 0.0, 0j, "", b"", [], (), {}, set()

falsy_values = [False, None, 0, 0.0, "", [], {}, ()]
for v in falsy_values:
    print(f"bool({v!r:10}) = {bool(v)}")

print()
# True 로 평가되는 값들 (비어있지 않은 모든 것):
truthy_values = [True, 1, -1, "0", "False", [0], {"a": 1}]
for v in truthy_values:
    print(f"bool({v!r:12}) = {bool(v)}")

# ──── 6. and / or — 단락 평가와 값 반환 ────
# and : 첫 번째 falsy 값을 반환; 모두 truthy 면 마지막 값 반환
# or  : 첫 번째 truthy 값을 반환; 모두 falsy 면 마지막 값 반환

print(0 and "hello")     # 0      (0 이 falsy → 즉시 반환)
print(1 and "hello")     # hello  (1 이 truthy → 다음 값 반환)
print(0 or "hello")      # hello  (0 이 falsy → 다음 값 탐색)
print("" or "익명")      # 익명   (빈 문자열 falsy → "익명" 반환)

# ──── 7. 체인 비교 ────
# Python 의 고유 기능 — 수학처럼 연결 가능

n = 7
print(1 < n < 10)        # True  — C에서는 (1 < n) and (n < 10) 이어야 함
print(1 < n < 5)         # False


if __name__ == "__main__":
    print("\n=== 불리언 데모 ===")

    # 체인 비교 활용
    for i in [0, 5, 10, 15]:
        in_range = 1 < i < 10
        print(f"1 < {i:2} < 10  →  {in_range}")

    print()

    # 기본값 패턴 (or 단락 평가)
    inputs = ["Alice", "", None, 0, "Bob"]
    for inp in inputs:
        display = inp or "익명"
        print(f"입력={inp!r:8} → 표시={display!r}")
