"""
concurrent.futures 모듈로 스레드/프로세스 풀을 간편하게 사용한다.
ThreadPoolExecutor 의 submit / map 패턴,
Future 객체로 결과를 가져오는 방법을 다룬다.
ProcessPoolExecutor 는 CPU-bound 에 사용하며 spawn 가드가 필요하다.
"""

import time
from concurrent.futures import ThreadPoolExecutor, Future

# ──── 1. ThreadPoolExecutor 기본 ────

def io_task(task_id: int, seconds: float = 0.3) -> str:
    """IO 를 시뮬레이션하는 함수 (실제로는 sleep)."""
    # 네트워크·파일 IO 처럼 대기가 많은 작업을 흉내
    time.sleep(seconds)
    return f"task-{task_id} 완료"


# ──── 2. submit 으로 Future 얻기 ────

def demo_submit() -> None:
    """submit() → Future → result() 패턴."""
    with ThreadPoolExecutor(max_workers=3) as executor:
        # submit: 작업을 풀에 제출하고 Future 반환
        futures: list[Future[str]] = [
            executor.submit(io_task, i) for i in range(3)
        ]
    # with 블록 종료 시 모든 작업이 완료될 때까지 자동 대기(shutdown)
    for fut in futures:
        print(f"  결과: {fut.result()}")   # Future.result() 로 반환값 획득


# ──── 3. map 으로 일괄 처리 ────

def demo_map() -> None:
    """executor.map() — 결과 순서가 입력 순서와 일치함."""
    task_ids = list(range(5))
    t0 = time.time()
    with ThreadPoolExecutor() as executor:
        # map: 이터러블 각 원소에 함수 적용, 결과는 생성기(generator)
        results = list(executor.map(io_task, task_ids))
    elapsed = time.time() - t0
    print(f"  결과: {results}")
    print(f"  5개 × 0.3s 작업 → 총 {elapsed:.2f}s (병렬 덕분에 ~0.3s)")


# ──── 4. ProcessPoolExecutor 언급 ────

# ProcessPoolExecutor 는 ThreadPoolExecutor 와 API 동일하지만
# 별도 프로세스로 실행 → GIL 회피 → CPU-bound 에 효과적.
# macOS/Windows 에서 'spawn' 방식이므로 반드시
# if __name__ == "__main__": 가드 안에서 사용해야 한다.
# 예:
#   from concurrent.futures import ProcessPoolExecutor
#   if __name__ == "__main__":
#       with ProcessPoolExecutor() as ex:
#           results = list(ex.map(cpu_heavy_fn, data))


if __name__ == "__main__":
    print("=== 1. submit + Future ===")
    demo_submit()

    print("\n=== 2. map 일괄 처리 (5개 IO 병렬) ===")
    demo_map()
