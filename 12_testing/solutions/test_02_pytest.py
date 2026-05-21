"""
정답 02 — pytest 입문.
"""


def test_str_upper():
    assert "hello".upper() == "HELLO"


def test_str_lower():
    assert "WORLD".lower() == "world"
