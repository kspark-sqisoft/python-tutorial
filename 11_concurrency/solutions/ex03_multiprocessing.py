"""
정답: Pool(2) 로 [1,2,3,4] 의 제곱을 병렬 계산.

왜 이렇게 하는가:
  - Pool(processes=2) 는 워커 프로세스를 2개 만든다.
  - pool.map(fn, iterable) 은 입력을 워커들에게 분배하고
    결과를 입력 순서대로 리스트로 반환한다.
  - 각 워커는 별도 프로세스이므로 GIL 의 영향을 받지 않는다.
  - macOS/Windows 의 'spawn' 시작 방식 때문에
    if __name__ == "__main__": 가드가 필수다.
"""

from multiprocessing import Pool


def square(x: int) -> int:
    return x * x


if __name__ == "__main__":
    with Pool(2) as pool:
        result = pool.map(square, [1, 2, 3, 4])

    assert result == [1, 4, 9, 16], f"결과 오류: {result}"
    print("OK")
