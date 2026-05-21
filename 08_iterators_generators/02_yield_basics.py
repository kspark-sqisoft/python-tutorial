"""
yield 와 제너레이터 함수 — 함수 안에서 yield 를 사용하면
호출 시 제너레이터 객체가 반환되고, 본문은 lazy 하게 실행된다.
next() 또는 for 로 값을 한 번에 하나씩 받아온다.
"""

# ──── 1. 제너레이터 함수 기본 ────

def simple_gen():
    """yield 가 있는 함수는 제너레이터 함수다."""
    print("  [A] 첫 번째 yield 전")
    yield 1           # 여기서 실행이 일시 정지되고 1 을 반환
    print("  [B] 두 번째 yield 전")
    yield 2
    print("  [C] 함수 끝")
    # 함수가 끝나면 StopIteration 자동 발생

# 호출해도 본문이 즉시 실행되지 않는다 — 제너레이터 객체만 반환
g = simple_gen()
print("제너레이터 객체:", g)

print("next() 첫 번째:")
print(" ", next(g))   # "[A]" 출력 후 1 반환

print("next() 두 번째:")
print(" ", next(g))   # "[B]" 출력 후 2 반환

print("next() 세 번째 — StopIteration:")
try:
    next(g)           # "[C]" 출력 후 StopIteration
except StopIteration:
    print("  StopIteration 발생")

# ──── 2. for 루프로 제너레이터 순회 ────

def count_up(limit):
    """0 부터 limit 미만까지 값을 하나씩 yield 한다."""
    i = 0
    while i < limit:
        yield i
        i += 1

print("\ncount_up(4) for 루프:")
for v in count_up(4):
    print(" ", v)

# ──── 3. my_range — range 처럼 동작하는 lazy 제너레이터 ────

def my_range(n):
    """내장 range 처럼 0 부터 n 미만 정수를 lazy 하게 yield."""
    i = 0
    while i < n:
        yield i
        i += 1

print("\nmy_range(5) 결과:", list(my_range(5)))

# ──── 4. 제너레이터는 값을 미리 만들지 않는다 ────

# range(10_000_000) 처럼 큰 범위도 메모리를 거의 사용하지 않는다
large_gen = my_range(1_000_000)   # 즉시 반환, 메모리 점유 최소
print("\n큰 범위 제너레이터 타입:", type(large_gen))
print("첫 값:", next(large_gen))  # 필요할 때만 계산


if __name__ == "__main__":
    print("\n=== 데모: my_range(5) for 순회 ===")
    for num in my_range(5):
        print(" ", num)
