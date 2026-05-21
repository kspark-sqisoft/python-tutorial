"""random 과 math 표준 라이브러리의 주요 기능을 익힌다.
random 은 난수 생성, math 는 수학 상수와 함수를 제공한다.
seed 를 고정하면 난수 결과를 재현할 수 있다.
"""

import random  # 난수 생성 모듈
import math    # 수학 함수·상수 모듈

# ──── 1. random 주요 함수 ────
# random.random()        — 0.0 이상 1.0 미만 부동소수점 난수
# random.randint(a, b)   — a 이상 b 이하 정수 난수 (양 끝 포함)
# random.choice(seq)     — 시퀀스에서 임의 요소 하나 선택
# random.sample(seq, k)  — 시퀀스에서 k 개 비복원 추출 (원본 변경 없음)
# random.shuffle(lst)    — 리스트를 제자리에서 섞음 (원본 변경)

# ──── 2. 시드 고정 ────
# random.seed(n) 으로 시드를 고정하면 이후 난수 결과가 항상 동일하다.
# 테스트·재현성이 필요할 때 사용한다.

# ──── 3. math 상수와 함수 ────
# math.pi          — 원주율 π ≈ 3.14159...
# math.e           — 자연상수 e ≈ 2.71828...
# math.sqrt(x)     — 제곱근
# math.floor(x)    — 내림 (정수)
# math.ceil(x)     — 올림 (정수)
# math.log(x)      — 자연로그 (밑 e); log(x, base) 로 밑 지정 가능
# math.factorial(n)— n! 팩토리얼

if __name__ == "__main__":
    # 시드 42 고정 후 randint 3번
    random.seed(42)
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    r3 = random.randint(1, 100)
    print(f"seed(42) randint ×3: {r1}, {r2}, {r3}")

    # choice / sample / shuffle 시연
    fruits = ["사과", "바나나", "체리", "포도", "딸기"]
    random.seed(42)
    print(f"choice:  {random.choice(fruits)}")
    print(f"sample 2: {random.sample(fruits, 2)}")

    lst = [1, 2, 3, 4, 5]
    random.shuffle(lst)
    print(f"shuffle: {lst}")

    print()
    # math 상수·함수
    print(f"math.pi          = {math.pi:.6f}")
    print(f"math.e           = {math.e:.6f}")
    print(f"math.sqrt(2)     = {math.sqrt(2):.6f}")
    print(f"math.floor(3.7)  = {math.floor(3.7)}")
    print(f"math.ceil(3.2)   = {math.ceil(3.2)}")
    print(f"math.log(math.e) = {math.log(math.e):.1f}")
    print(f"math.factorial(6)= {math.factorial(6)}")
