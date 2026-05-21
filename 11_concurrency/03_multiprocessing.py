"""
multiprocessing 모듈로 별도 프로세스를 생성한다.
각 프로세스는 독립적인 메모리를 가지므로 GIL 에 구애받지 않는다.
CPU-bound 작업에 효과적이며, macOS/Windows 의 spawn 방식 때문에
모든 실행 코드는 if __name__ == "__main__": 가드 안에 있어야 한다.
"""

from multiprocessing import Process, Pool

# ──── 1. Process 직접 생성 ────

def worker_process(name: str) -> None:
    """별도 프로세스에서 실행되는 함수."""
    # 각 Process 는 완전히 분리된 메모리 공간에서 실행됨
    print(f"  프로세스 [{name}] 실행 중")


# ──── 2. Pool 로 일괄 CPU 작업 ────

def square(x: int) -> int:
    """x 의 제곱을 반환하는 가벼운 CPU 작업."""
    return x * x


def sum_range(n: int) -> int:
    """1 부터 n 까지의 합 (CPU 계산 시뮬레이션)."""
    return sum(range(1, n + 1))


# ──── 3. 데이터 공유 방법 (언급만) ────

# 프로세스 간 메모리는 분리되어 있어 일반 변수 공유 불가.
# 데이터를 주고받는 방법:
#   - Queue  : 프로세스 간 메시지 큐
#   - Pipe   : 양방향 파이프 통신
#   - Manager: 공유 딕셔너리·리스트 (느리지만 편리)
#   - Pool.map 의 반환값: 가장 단순하고 권장되는 방식


if __name__ == "__main__":
    # ── Process 직접 생성 ──
    print("=== 1. Process 직접 생성 ===")
    p1 = Process(target=worker_process, args=("Alpha",))
    p2 = Process(target=worker_process, args=("Beta",))
    p1.start()
    p2.start()
    p1.join()   # 메인이 p1 완료를 기다림
    p2.join()

    # ── Pool 로 CPU 작업 병렬화 ──
    print("\n=== 2. Pool(2) 로 제곱 계산 병렬 처리 ===")
    data = [1, 2, 3, 4, 5]
    with Pool(processes=2) as pool:
        # pool.map: data 각 원소에 square 적용 → 결과 리스트
        squares = pool.map(square, data)
    print(f"  입력:  {data}")
    print(f"  제곱:  {squares}")

    print("\n=== 3. Pool(2) 로 두 작업 병렬 실행 ===")
    tasks = [1_000_000, 2_000_000]   # 각각 1~N 합산
    with Pool(processes=2) as pool:
        results = pool.map(sum_range, tasks)
    for n, r in zip(tasks, results):
        print(f"  sum(1..{n:,}) = {r:,}")
