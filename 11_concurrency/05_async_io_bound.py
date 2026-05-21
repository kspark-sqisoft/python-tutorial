"""
asyncio 를 활용한 IO-bound 작업 최적화.
가짜 "네트워크 호출" 10개를 동기(순차) vs 비동기(gather) 로 실행해
실질적인 속도 차이를 확인한다.
async for / async with 의 존재도 간략히 소개한다.
"""

import asyncio
import time

# ──── 1. 가짜 IO 작업 ────

async def fake_network_call(call_id: int, delay: float = 0.2) -> int:
    """네트워크 응답을 흉내내는 코루틴. delay 초 후 call_id 를 반환."""
    # 실제 네트워크 라이브러리(aiohttp 등)도 내부적으로 await 을 사용함
    await asyncio.sleep(delay)
    return call_id


# ──── 2. 동기 방식 (비교 기준) ────

def sync_sequential(n: int, delay: float) -> float:
    """time.sleep 을 n 번 순차 호출. 총 경과 시간 반환."""
    t0 = time.perf_counter()
    for _ in range(n):
        time.sleep(delay)   # 블로킹 sleep — 이벤트 루프 없음
    return time.perf_counter() - t0


# ──── 3. 비동기 방식 ────

async def async_gather(n: int, delay: float) -> tuple[int, float]:
    """gather 로 n 개 코루틴 동시 실행. (결과 합, 경과 시간) 반환."""
    t0 = time.perf_counter()
    results = await asyncio.gather(
        *(fake_network_call(i, delay) for i in range(n))
    )
    elapsed = time.perf_counter() - t0
    return sum(results), elapsed


# ──── 4. async for / async with (한 줄 소개) ────

# async for  : 비동기 이터러블을 순회 (예: 스트리밍 응답)
#   async for chunk in response.content: ...
#
# async with : 비동기 컨텍스트 매니저 (예: DB 커넥션, HTTP 세션)
#   async with aiohttp.ClientSession() as session: ...


# ──── 5. 비교 표 출력 ────

async def compare() -> None:
    n, delay = 10, 0.2

    print(f"  작업 수: {n}개 / 작업당 대기: {delay}s")
    print(f"  {'방식':<12} {'경과 시간':>10}  {'예상 시간':>10}")
    print(f"  {'-'*36}")

    # 동기 순차
    sync_elapsed = sync_sequential(n, delay)
    print(f"  {'동기(순차)':<12} {sync_elapsed:>9.2f}s  {n * delay:>9.1f}s")

    # 비동기 gather
    total, async_elapsed = await async_gather(n, delay)
    print(f"  {'비동기(gather)':<12} {async_elapsed:>9.2f}s  {'~' + str(delay) + 's':>10}")
    print(f"\n  결과 합계: {total}  (0+1+…+{n-1} = {n*(n-1)//2})")
    print(f"  → 비동기가 약 {sync_elapsed / async_elapsed:.0f}배 빠름")


if __name__ == "__main__":
    print("=== 동기 vs 비동기 IO-bound 비교 ===\n")
    asyncio.run(compare())
