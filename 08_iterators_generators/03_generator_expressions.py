"""
제너레이터 표현식 — 리스트 컴프리헨션과 문법은 비슷하지만
대괄호 대신 소괄호를 쓴다. 값을 미리 만들지 않아 메모리를 절약한다.
sum/max/any/all 같은 함수에 바로 넘길 수 있다.
"""

import sys  # 메모리 크기 비교용

# ──── 1. 기본 문법 ────

# 리스트 컴프리헨션: 모든 값을 즉시 계산해 메모리에 저장
squares_list = [x * x for x in range(10)]
print("리스트:", squares_list)

# 제너레이터 표현식: 소괄호 사용, lazy 평가
squares_gen = (x * x for x in range(10))
print("제너레이터:", squares_gen)          # generator 객체
print("첫 번째 값:", next(squares_gen))    # 필요할 때 계산

# ──── 2. 메모리 사용량 비교 ────

n = 10_000  # 안전한 크기로 시연
list_size = sys.getsizeof([x * x for x in range(n)])
gen_size  = sys.getsizeof((x * x for x in range(n)))

print(f"\nn={n} 기준 메모리 비교:")
print(f"  리스트:       {list_size:>8} bytes")
print(f"  제너레이터:   {gen_size:>8} bytes")

# ──── 3. 집계 함수에 바로 넘기기 ────

# sum, max, min, any, all 은 이터러블을 받으므로 제너레이터를 그대로 전달 가능
total  = sum(x * x for x in range(1, 11))   # 1²+2²+…+10²
maximum = max(x * x for x in range(1, 11))
print(f"\n1~10 제곱의 합:  {total}")
print(f"1~10 제곱의 최댓값: {maximum}")

# any / all
has_large = any(x > 90 for x in range(1, 101))   # 91~100 이 있으므로 True
all_even  = all(x % 2 == 0 for x in [2, 4, 6])   # 모두 짝수
print(f"\n100 이하 범위에 90 초과 수 있음: {has_large}")
print(f"[2, 4, 6] 모두 짝수:             {all_even}")

# ──── 4. 조건 필터 포함 ────

# 짝수 제곱만 합산 — 중간 리스트 없이 한 줄로
even_sq_sum = sum(x * x for x in range(1, 101) if x % 2 == 0)
print(f"\n1~100 짝수 제곱의 합: {even_sq_sum}")

# ──── 5. 중첩 제너레이터 표현식 ────

# (row, col) 쌍 생성 — 3×3 격자
pairs = list((r, c) for r in range(3) for c in range(3))
print(f"\n3×3 격자 쌍 (처음 4개): {pairs[:4]} ...")


if __name__ == "__main__":
    print("\n=== 데모: 1~10000 제곱의 합 ===")
    result = sum(x * x for x in range(1, 10_001))
    print(f"  sum(x*x for x in range(1, 10001)) = {result}")
