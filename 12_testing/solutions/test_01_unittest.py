"""
정답 01 — unittest 기본.
"""

import unittest


def multiply(a: int, b: int) -> int:
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add_works(self):
        self.assertEqual(1 + 1, 2)

    def test_multiply_works(self):
        self.assertEqual(multiply(3, 4), 12)


if __name__ == "__main__":
    unittest.main(exit=False)
