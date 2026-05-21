"""연습: asyncio.gather 로 두 코루틴을 동시 실행하고 시간을 측정한다."""

import asyncio
import time


async def slow_task(name: str) -> str:
    """0.3초 후 name 을 반환하는 코루틴."""
    await asyncio.sleep(0.3)
    return name


async def main() -> None:
    t0 = time.perf_counter()

    # TODO: slow_task("A") 와 slow_task("B") 를 gather 로 동시 실행하고
    #       결과를 result_a, result_b 에 저장한다.

    # --- 여기에 코드 작성 ---
    result_a = None
    result_b = None
    # ----------------------

    elapsed = time.perf_counter() - t0

    assert result_a == "A", f"결과 오류: {result_a}"
    assert result_b == "B", f"결과 오류: {result_b}"
    assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s (gather 면 ~0.3s 여야 함)"
    print("OK")


if __name__ == "__main__":
    asyncio.run(main())
