"""연습: 5개 가짜 IO 작업을 gather 로 동시 실행하고 결과 합과 시간을 검증한다."""

import asyncio
import time


async def fetch(item_id: int) -> int:
    """0.2초 후 item_id 를 반환하는 가짜 IO 코루틴."""
    await asyncio.sleep(0.2)
    return item_id


async def main() -> None:
    t0 = time.perf_counter()

    # TODO: fetch(0) ~ fetch(4) 를 gather 로 동시 실행하고
    #       반환값의 합을 total 에 저장한다.

    # --- 여기에 코드 작성 ---
    total = None
    # ----------------------

    elapsed = time.perf_counter() - t0

    assert total == 0 + 1 + 2 + 3 + 4, f"결과 오류: {total}"
    assert elapsed < 0.5, f"너무 느림: {elapsed:.2f}s (gather 면 ~0.2s 여야 함)"
    print("OK")


if __name__ == "__main__":
    asyncio.run(main())
