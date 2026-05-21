# 12_testing — 테스트 (pytest)

## 사전 준비

```bash
uv pip install -e ".[test]"
```

## 배우는 것

- unittest 기본 (표준 라이브러리)
- pytest 입문 — test_ 자동 수집 + 평범한 assert
- 픽스처 (@pytest.fixture, scope, yield)
- 모킹 (unittest.mock + patch)
- 매개변수화 (@pytest.mark.parametrize)

## 학습 순서

1. `01_unittest_basics.py`
2. `02_pytest_basics.py`
3. `03_fixtures.py`
4. `04_mocking.py`
5. `05_parametrize.py`

## 실행 방법

학습 스크립트는 평소처럼 — 내부에서 pytest.main 을 호출한다:

```bash
uv run python 12_testing/02_pytest_basics.py
```

## 연습문제 (pytest 컨벤션)

이 폴더만 연습문제가 OK 패턴 대신 pytest 의 `test_*.py` 형식을 따른다:

```bash
uv run pytest 12_testing/exercises/ -q
uv run pytest 12_testing/solutions/ -q
```

- 미완성 연습은 일부 테스트가 실패한다.
- 풀이를 채우면 모두 통과한다.
- `solutions/` 와 비교.
