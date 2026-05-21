"""
asyncio 기초: 이벤트 루프, 코루틴, gather.
async/await 키워드로 비동기 함수를 정의하고,
asyncio.run() 으로 이벤트 루프를 시작하는 방법을 다룬다.
asyncio.gather 로 여러 코루틴을 동시에 실행한다.
"""

import asyncio
import time

# ──── 1. async def / await ────

async def greet(name: str, delay: float) -> str:
    """delay 초 후 인사 메시지를 반환하는 코루틴."""
    # await asyncio.sleep: 이벤트 루프에 제어권을 돌려주는 비차단 대기
    # threading.sleep 과 달리 스레드를 블로킹하지 않음
    await asyncio.sleep(delay)
    message = f"안녕하세요, {name}!"
    print(f"  {message}")
    return message


# ──── 2. asyncio.run ────

# asyncio.run(coroutine): 이벤트 루프를 생성하고 코루틴을 실행한 뒤 닫는다.
# 최상위 진입점으로 주로 사용.


# ──── 3. asyncio.gather ────

async def demo_gather() -> None:
    """3개 코루틴을 gather 로 동시 실행 → ~0.3s."""
    print("  gather 시작...")
    t0 = time.perf_counter()

    # gather: 여러 코루틴을 동시에 스케줄링하고 모든 결과를 리스트로 반환
    results = await asyncio.gather(
        greet("Alice", 0.3),
        greet("Bob",   0.3),
        greet("Carol", 0.3),
    )

    elapsed = time.perf_counter() - t0
    print(f"  결과: {results}")
    print(f"  3개 × 0.3s → 총 {elapsed:.2f}s (gather 덕분에 ~0.3s)")


# ──── 4. 순차 실행과 비교 ────

async def demo_sequential() -> None:
    """코루틴을 순서대로 await → ~0.9s (비교용)."""
    t0 = time.perf_counter()
    await greet("순차-A", 0.3)
    await greet("순차-B", 0.3)
    await greet("순차-C", 0.3)
    elapsed = time.perf_counter() - t0
    print(f"  순차 실행 → 총 {elapsed:.2f}s")


if __name__ == "__main__":
    print("=== 1. 순차 실행 ===")
    asyncio.run(demo_sequential())

    print("\n=== 2. gather 동시 실행 ===")
    asyncio.run(demo_gather())
