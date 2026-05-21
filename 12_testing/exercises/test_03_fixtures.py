"""
연습 03 — pytest 픽스처.
numbers 픽스처는 완성되어 있다.
test_sum_works 의 TODO 를 채워 테스트를 통과시켜라.
"""

import pytest


@pytest.fixture
def numbers() -> list[int]:
    # 완성된 픽스처 — 수정하지 말 것
    return [10, 20, 30]


def test_sum_works(numbers: list[int]):
    # TODO: numbers 리스트의 합이 60 임을 assert 로 검증하라.
    assert False, "TODO: assert sum(numbers) == 60 을 작성하라"
