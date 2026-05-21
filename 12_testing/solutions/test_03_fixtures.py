"""
정답 03 — pytest 픽스처.
"""

import pytest


@pytest.fixture
def numbers() -> list[int]:
    return [10, 20, 30]


def test_sum_works(numbers: list[int]):
    assert sum(numbers) == 60
