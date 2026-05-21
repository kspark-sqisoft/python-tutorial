"""
numpy 기초: 배열 생성, shape/dtype, 벡터화 연산,
인덱싱·슬라이싱·불리언 마스킹을 다룬다.
Python 루프 대신 numpy 벡터 연산이 훨씬 빠름을 이해한다.
"""

import numpy as np

# ──── 1. 배열 생성 ────

def section_creation() -> None:
    # 리스트로부터 1D 배열 생성
    a = np.array([1, 2, 3, 4, 5])
    print("1D array:", a)

    # 2D 배열 (행렬)
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D array:\n", mat)

    # 0으로 채운 배열
    zeros = np.zeros((3, 4))
    print("zeros (3x4):\n", zeros)

    # 1로 채운 배열
    ones = np.ones(5)
    print("ones (5):", ones)

    # 등간격 정수 (arange)
    rng = np.arange(0, 10, 2)   # 0부터 10 미만, 간격 2
    print("arange(0,10,2):", rng)

    # 등간격 실수 (linspace)
    lin = np.linspace(0, 1, 5)  # 0~1 사이를 5개로 균등 분할
    print("linspace(0,1,5):", lin)


# ──── 2. shape / dtype / reshape ────

def section_shape_dtype() -> None:
    a = np.arange(12)
    print("원본 shape:", a.shape, "dtype:", a.dtype)

    # reshape: 원소 수가 같으면 어떤 형태든 가능
    mat = a.reshape((3, 4))
    print("reshape(3,4):\n", mat)
    print("새 shape:", mat.shape)

    # dtype 지정
    f = np.array([1, 2, 3], dtype=np.float64)
    print("float64 array:", f, "dtype:", f.dtype)


# ──── 3. 벡터화 연산 ────

def section_vectorized() -> None:
    a = np.array([1, 4, 9, 16, 25])
    b = np.array([1, 2, 3, 4, 5])

    print("a + b:", a + b)          # 원소별 덧셈
    print("a * 2:", a * 2)          # 스칼라 곱
    print("sqrt(a):", np.sqrt(a))   # 원소별 제곱근

    # Python 루프 대신 numpy 연산이 수십~수백 배 빠름
    # (내부적으로 C/BLAS 로 최적화)


# ──── 4. 인덱싱 · 슬라이싱 · 불리언 마스킹 ────

def section_indexing() -> None:
    a = np.array([10, 20, 30, 40, 50])

    print("a[0]:", a[0])          # 첫 번째 원소
    print("a[-1]:", a[-1])        # 마지막 원소
    print("a[1:4]:", a[1:4])      # 슬라이스 (index 1~3)

    # 2D 슬라이싱
    mat = np.arange(1, 10).reshape((3, 3))
    print("2D mat:\n", mat)
    print("mat[0, :]:", mat[0, :])    # 첫 번째 행
    print("mat[:, 1]:", mat[:, 1])    # 두 번째 열

    # 불리언 마스킹: 조건에 맞는 원소만 추출
    mask = a > 25
    print("a > 25 mask:", mask)
    print("a[a > 25]:", a[a > 25])


if __name__ == "__main__":
    print("=" * 45)
    print("1. 배열 생성")
    print("=" * 45)
    section_creation()

    print("\n" + "=" * 45)
    print("2. shape / dtype / reshape")
    print("=" * 45)
    section_shape_dtype()

    print("\n" + "=" * 45)
    print("3. 벡터화 연산")
    print("=" * 45)
    section_vectorized()

    print("\n" + "=" * 45)
    print("4. 인덱싱 · 슬라이싱 · 불리언 마스킹")
    print("=" * 45)
    section_indexing()
