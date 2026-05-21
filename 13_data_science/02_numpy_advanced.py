"""
numpy 심화: 브로드캐스팅, 축(axis) 집계,
행렬 곱, 난수 생성을 다룬다.
다차원 배열 연산의 핵심 규칙을 이해한다.
"""

import numpy as np

# ──── 1. 브로드캐스팅 ────

def section_broadcasting() -> None:
    # 브로드캐스팅: 형태가 다른 배열 간 연산 시 작은 배열을 자동 확장
    # 규칙: 뒤쪽 차원부터 비교해 1이거나 같으면 확장 가능
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])        # shape (2, 3)
    b = np.array([10, 20, 30])       # shape (3,) → (1,3) → (2,3) 으로 확장

    print("a shape:", a.shape, "  b shape:", b.shape)
    print("a + b (브로드캐스팅):\n", a + b)

    # 열 벡터와 행 벡터 → 외적 형태
    col = np.array([[1], [2], [3]])  # shape (3, 1)
    row = np.array([10, 20, 30])     # shape (3,)
    print("col * row:\n", col * row)


# ──── 2. 집계 함수 ────

def section_aggregation() -> None:
    a = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

    print("전체 합:", a.sum())
    print("전체 평균:", a.mean())
    print("표준편차:", a.std())
    print("최솟값:", a.min(), " 최댓값:", a.max())
    print("최솟값 인덱스 (flatten):", a.argmin())
    print("최댓값 인덱스 (flatten):", a.argmax())

    # axis=0 → 열 방향 집계 (각 열의 통계)
    print("열별 합 (axis=0):", a.sum(axis=0))
    # axis=1 → 행 방향 집계 (각 행의 통계)
    print("행별 합 (axis=1):", a.sum(axis=1))
    print("행별 평균 (axis=1):", a.mean(axis=1))


# ──── 3. 행렬 곱 ────

def section_matmul() -> None:
    A = np.array([[1, 2],
                  [3, 4]])   # (2,2)
    B = np.array([[5, 6],
                  [7, 8]])   # (2,2)

    # @ 연산자: 행렬 곱 (Python 3.5+)
    print("A @ B:\n", A @ B)
    # np.dot 도 동일
    print("np.dot(A,B):\n", np.dot(A, B))

    # 벡터 내적
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print("v1 · v2:", v1 @ v2)   # 1*4+2*5+3*6 = 32


# ──── 4. 난수 생성 ────

def section_random() -> None:
    # 권장 방식: default_rng(seed) 로 재현 가능한 난수 생성기 사용
    rng = np.random.default_rng(seed=42)

    # 정규분포 샘플
    samples = rng.normal(loc=0.0, scale=1.0, size=5)
    print("정규분포 샘플(5):", samples)

    # 균등분포 정수
    ints = rng.integers(0, 10, size=6)
    print("균등 정수(0~9, 6개):", ints)

    # 2D 난수 배열
    mat = rng.random((3, 3))   # [0, 1) 균등분포
    print("2D 난수(3x3):\n", mat)


if __name__ == "__main__":
    print("=" * 45)
    print("1. 브로드캐스팅")
    print("=" * 45)
    section_broadcasting()

    print("\n" + "=" * 45)
    print("2. 집계 함수")
    print("=" * 45)
    section_aggregation()

    print("\n" + "=" * 45)
    print("3. 행렬 곱")
    print("=" * 45)
    section_matmul()

    print("\n" + "=" * 45)
    print("4. 난수 생성")
    print("=" * 45)
    section_random()
