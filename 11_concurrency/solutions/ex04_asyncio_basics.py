"""
정답: asyncio.gather 로 두 코루틴을 동시 실행.

왜 이렇게 하는가:
  - asyncio.gather(*coroutines) 는 모든 코루틴을 이벤트 루프에
    동시에 스케줄링하고, 전부 완료되면 결과 리스트를 반환한다.
  - 두 코루틴이 각각 0.3s sleep 하지만 동시에 실행되므로
    총 대기 시간은 ~0.3s (순차 await 이면 ~0.6s).
  - gather 의 반환값은 인수 순서와 동일하므로 언패킹으로 받을 수 있다.
"""

import asyncio
import time


async def slow_task(name: str) -> str:
    await asyncio.sleep(0.3)
    return name


async def main() -> None:
    t0 = time.perf_counter()

    result_a, result_b = await asyncio.gather(
        slow_task("A"),
        slow_task("B"),
    )

    elapsed = time.perf_counter() - t0

    assert result_a == "A", f"결과 오류: {result_a}"
    assert result_b == "B", f"결과 오류: {result_b}"
    assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s"
    print("OK")


if __name__ == "__main__":
    asyncio.run(main())
