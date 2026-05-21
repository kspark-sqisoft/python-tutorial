"""연습: Pool(2) 로 [1,2,3,4] 의 제곱을 병렬 계산한다."""

from multiprocessing import Pool


def square(x: int) -> int:
    """x 의 제곱을 반환."""
    return x * x


if __name__ == "__main__":
    # TODO: Pool(2) 를 사용해 [1, 2, 3, 4] 각 원소의 제곱을 병렬 계산하고
    #       결과를 result 에 저장한다.
    #       (pool.map 사용)

    # --- 여기에 코드 작성 ---
    result = None
    # ----------------------

    assert result == [1, 4, 9, 16], f"결과 오류: {result}"
    print("OK")
