# 11_concurrency — 동시성

## 배우는 것

- threading + GIL 의미 (IO-bound 에 효과)
- concurrent.futures (ThreadPoolExecutor / ProcessPoolExecutor)
- multiprocessing (CPU-bound, 별도 메모리, spawn 가드)
- asyncio (async/await, asyncio.run, gather)
- 동기 vs 비동기 IO 비교

## 학습 순서

1. `01_threading.py`
2. `02_concurrent_futures.py`
3. `03_multiprocessing.py`
4. `04_asyncio_basics.py`
5. `05_async_io_bound.py`

## 실행 방법

```bash
uv run python 11_concurrency/01_threading.py
uv run python 11_concurrency/02_concurrent_futures.py
uv run python 11_concurrency/03_multiprocessing.py
uv run python 11_concurrency/04_asyncio_basics.py
uv run python 11_concurrency/05_async_io_bound.py
```

## 주의

- 멀티프로세싱 예제는 `if __name__ == "__main__":` 가드 안에서만 실행됩니다 (macOS/Windows 의 spawn 방식 요구).
- 시간 측정 assert 는 여유를 두었지만 매우 느린 환경에서는 흔들릴 수 있습니다.

## 연습문제

- `exercises/ex01_*.py` ~ `ex05_*.py` 의 TODO 를 채워 `OK` 가 출력되게 만든다.
- 막히면 `solutions/` 와 비교.
