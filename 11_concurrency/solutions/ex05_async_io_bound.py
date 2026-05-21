"""
정답: 5개 가짜 IO 코루틴을 gather 로 동시 실행.

왜 이렇게 하는가:
  - asyncio.gather 에 제너레이터 표현식으로 코루틴 5개를 전달한다.
  - 모두 동시에 스케줄링되므로 총 대기 시간은 ~0.2s (순차면 ~1.0s).
  - sum(results) 로 반환값을 합산한다 (0+1+2+3+4 = 10).
  - IO-bound 작업에서 asyncio 가 얼마나 효율적인지 보여주는 전형적인 패턴이다.
"""

import asyncio
import time


async def fetch(item_id: int) -> int:
    await asyncio.sleep(0.2)
    return item_id


async def main() -> None:
    t0 = time.perf_counter()

    results = await asyncio.gather(*(fetch(i) for i in range(5)))
    total = sum(results)

    elapsed = time.perf_counter() - t0

    assert total == 0 + 1 + 2 + 3 + 4, f"결과 오류: {total}"
    assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s"
    print("OK")


if __name__ == "__main__":
    asyncio.run(main())
