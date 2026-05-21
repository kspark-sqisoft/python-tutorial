"""
연습 04 — 모킹.
patch 로 get_price 를 모킹하는 테스트에서 TODO 를 채워 통과시켜라.
"""

from unittest.mock import patch


def get_price(item: str) -> float:
    """외부 API 에서 가격을 가져온다고 가정."""
    raise NotImplementedError("실제 구현은 외부 I/O 필요")


def calculate_total(item: str, quantity: int) -> float:
    """단가 × 수량으로 총액을 계산한다."""
    price = get_price(item)
    return price * quantity


def test_calculate_total_mocked():
    with patch(f"{__name__}.get_price") as mock_get_price:
        mock_get_price.return_value = 5.0
        result = calculate_total("apple", 3)
        # TODO: result 가 15.0 임을 assert 로 검증하라.
        assert False, "TODO: assert result == 15.0 을 작성하라"
        # TODO: mock_get_price 가 "apple" 인자로 호출됐는지 assert_called_with 로 검증하라.
