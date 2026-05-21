"""
함수 데코레이터(Decorator) 학습 모듈.
@deco 문법이 f = deco(f) 와 동일함을 이해하고,
단순 데코레이터 / 인자 받는 데코레이터 / functools.wraps 를 다룬다.
"""

import functools

# ──── 1. 데코레이터란? ────

# 데코레이터 = 함수를 받아 함수를 반환하는 함수
# @log 는 add = log(add) 와 완전히 동일하다

def log(fn):
    """호출 시 함수 이름을 출력하는 단순 데코레이터."""
    def wrapper(*args, **kwargs):   # *args, **kwargs 로 모든 인자를 그대로 전달
        print(f"[log] {fn.__name__} 호출됨")
        return fn(*args, **kwargs)
    return wrapper


@log
def add(a, b):
    """두 수를 더한다."""
    return a + b


# ──── 2. 인자를 받는 데코레이터 (3중 중첩) ────

# 데코레이터 자체가 인자를 받으려면 한 겹 더 감싸야 한다
# @repeat(3)  →  add = repeat(3)(add)

def repeat(n):
    """fn 을 n 번 반복 호출하는 데코레이터 팩토리."""
    def deco(fn):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):          # n 번 반복
                result = fn(*args, **kwargs)
            return result               # 마지막 반환값
        return wrapper
    return deco


@repeat(3)
def say(msg):
    """메시지를 출력한다."""
    print(msg)


# ──── 3. functools.wraps — 원본 함수 메타데이터 보존 ────

# 데코레이터를 적용하면 __name__, __doc__ 이 wrapper 로 덮여버린다
# functools.wraps(fn) 을 wrapper 에 달면 원본 정보가 보존된다

def log_with_wraps(fn):
    """functools.wraps 를 사용하는 개선된 로그 데코레이터."""
    @functools.wraps(fn)            # fn 의 __name__, __doc__ 을 wrapper 에 복사
    def wrapper(*args, **kwargs):
        print(f"[log] {fn.__name__} 호출됨")
        return fn(*args, **kwargs)
    return wrapper


@log_with_wraps
def multiply(a, b):
    """두 수를 곱한다."""
    return a * b


# ──── 4. @staticmethod, @classmethod 한마디 ────

# @staticmethod : 인스턴스/클래스 참조 없이 클래스 이름공간에 묶인 함수
# @classmethod  : 첫 인자로 클래스(cls)를 받는 메서드 — 자세한 내용은 05_oop 참고


# ──── 5. __name__ 비교 ────

def plain_log(fn):
    """wraps 없는 데코레이터 (메타데이터 손실)."""
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


@plain_log
def subtract(a, b):
    """두 수를 뺀다."""
    return a - b


if __name__ == "__main__":
    # 단순 데코레이터 시연
    print("=== @log ===")
    result = add(3, 4)
    print(f"add(3, 4) = {result}")

    print()

    # 인자 받는 데코레이터 시연
    print("=== @repeat(3) ===")
    say("안녕!")

    print()

    # functools.wraps 비교 시연
    print("=== functools.wraps 비교 ===")
    print(f"wraps 없음  → subtract.__name__ = {subtract.__name__}")   # 'wrapper'
    print(f"wraps 있음  → multiply.__name__ = {multiply.__name__}")   # 'multiply'
    print(f"multiply.__doc__ = {multiply.__doc__}")

    print()

    # 실제 동작 확인
    print("=== multiply 호출 ===")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
