"""
재귀 (Recursion)
- 재귀는 함수가 자기 자신을 호출하는 기법으로, 종료조건 + 자기호출 두 부분으로 구성된다.
- 파이썬은 기본 재귀 한계가 약 1000이며, 꼬리 재귀 최적화(TCO)를 지원하지 않는다.
- C++/Java 의 일부 컴파일러는 TCO를 적용하지만 파이썬은 스택을 그대로 쌓는다.
- 큰 입력에는 반복문(iterative) 버전을 권장한다.
"""

import sys  # sys.getrecursionlimit() 확인용

# ──── 1. 팩토리얼 ────

def factorial(n):
    """n! 을 재귀로 계산한다. 종료조건: n <= 1."""
    if n <= 1:          # 종료조건 (base case) — 없으면 무한 호출
        return 1
    return n * factorial(n - 1)   # 자기호출 (recursive case)


# 비교용: 반복문 버전 (큰 n 에 안전)
def factorial_iter(n):
    """n! 을 반복문으로 계산한다."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ──── 2. 피보나치 (느린 버전) ────

def fib(n):
    """n 번째 피보나치 수를 재귀로 반환한다. 중복 호출이 많아 느리다."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# ──── 3. 파이썬 재귀 한계 ────

# sys.getrecursionlimit() 은 보통 1000
# factorial(1000) 은 RecursionError 발생
# sys.setrecursionlimit(n) 으로 늘릴 수 있지만 권장하지 않음


# ──── 4. 재귀의 장단점 ────

# 장점: 트리·그래프 탐색, 분할정복 등 자연스러운 표현
# 단점: 스택 오버플로 위험, 호출 오버헤드, TCO 없음
# → 실무에서는 반복문 또는 메모이제이션(functools.lru_cache) 사용 권장


if __name__ == "__main__":
    # ── 팩토리얼 ──
    print(factorial(10))        # 3628800
    print(factorial_iter(10))   # 3628800 — 동일

    # ── 피보나치 ──
    print(fib(10))              # 55
    fib_seq = [fib(i) for i in range(11)]
    print(fib_seq)              # [0,1,1,2,3,5,8,13,21,34,55]

    # ── 재귀 한계 확인 ──
    limit = sys.getrecursionlimit()
    print(f"기본 재귀 한계: {limit}")   # 보통 1000

    # ── 큰 입력: 반복문이 안전 ──
    print(factorial_iter(500))  # 정상 동작 (반복문)
    # factorial(500) 은 한계에 걸릴 수 있다
