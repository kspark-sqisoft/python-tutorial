"""
스코프와 클로저 (Scope & Closure)
- 파이썬은 LEGB 규칙으로 이름을 탐색한다: Local → Enclosing → Global → Built-in
- global/nonlocal 키워드로 바깥 스코프의 변수를 명시적으로 수정할 수 있다.
- 클로저는 내부 함수가 둘러싼 함수의 변수를 '캡처'해 생명을 연장시킨다.
- Java 람다의 effectively-final 규칙과 달리 nonlocal 로 캡처 변수 수정이 가능하다.
"""

# ──── 1. LEGB 규칙 ────

x = "전역(Global)"          # G — 전역 변수

def outer():
    x = "둘러싼(Enclosing)"  # E — outer 스코프

    def inner():
        x = "지역(Local)"    # L — inner 스코프
        print(x)             # Local 이 먼저 탐색됨

    inner()
    print(x)                 # Enclosing

# Built-in 예: len, print 등 파이썬이 기본 제공하는 이름


# ──── 2. global 키워드 ────

count = 0   # 전역 카운터

def increment_global():
    global count            # 전역 변수를 수정하겠다는 선언
    count += 1


# ──── 3. nonlocal 키워드 ────

def make_counter_nonlocal():
    """nonlocal 로 둘러싼 변수를 수정하는 예제."""
    n = 0

    def step():
        nonlocal n          # 둘러싼 함수의 n 을 수정하겠다는 선언
        n += 1
        return n

    return step


# ──── 4. 클로저 (Closure) ────
# 내부 함수가 둘러싼 함수의 변수를 기억하고 있는 함수 객체

def make_counter(start=0):
    """독립적인 카운터 함수를 반환한다."""
    current = start         # 클로저가 캡처할 변수

    def counter():
        nonlocal current
        current += 1
        return current

    return counter          # counter 함수(+ 캡처된 current)를 반환


def make_greeter(greeting):
    """특정 인사말을 고정한 인사 함수를 반환한다."""
    def greet(name):
        return f"{greeting}, {name}!"
    return greet


if __name__ == "__main__":
    # ── LEGB ──
    outer()
    print(x)                # 전역(Global) — 바깥은 영향받지 않음

    # ── global ──
    print(f"증가 전: {count}")   # 0
    increment_global()
    increment_global()
    print(f"증가 후: {count}")   # 2

    # ── nonlocal ──
    step = make_counter_nonlocal()
    print(step())   # 1
    print(step())   # 2
    print(step())   # 3

    # ── 클로저: 여러 카운터가 독립적 ──
    c1 = make_counter()       # 0 에서 시작
    c2 = make_counter(10)     # 10 에서 시작

    print(c1())   # 1
    print(c1())   # 2
    print(c2())   # 11   ← c1 과 무관하게 독립적
    print(c1())   # 3
    print(c2())   # 12

    # ── 인사 클로저 ──
    hi = make_greeter("안녕")
    hello = make_greeter("Hello")
    print(hi("지수"))       # 안녕, 지수!
    print(hello("민준"))    # Hello, 민준!
