"""
정답 04 — 모킹.
"""

from unittest.mock import patch


def get_price(item: str) -> float:
    raise NotImplementedError("실제 구현은 외부 I/O 필요")


def calculate_total(item: str, quantity: int) -> float:
    price = get_price(item)
    return price * quantity


def test_calculate_total_mocked():
    with patch(f"{__name__}.get_price") as mock_get_price:
        mock_get_price.return_value = 5.0
        result = calculate_total("apple", 3)
        assert result == 15.0
        mock_get_price.assert_called_with("apple")
