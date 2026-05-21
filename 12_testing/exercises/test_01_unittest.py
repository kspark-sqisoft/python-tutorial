"""
연습 01 — unittest 기본.
test_add_works 는 완성되어 있다.
test_multiply_works 의 TODO 를 채워 테스트를 통과시켜라.
"""

import unittest


def multiply(a: int, b: int) -> int:
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add_works(self):
        # 완성된 테스트 — 수정하지 말 것
        self.assertEqual(1 + 1, 2)

    def test_multiply_works(self):
        # TODO: multiply(3, 4) 의 결과가 12 임을 assertEqual 로 검증하라.
        self.fail("TODO: assertEqual 로 multiply(3, 4) == 12 를 검증하라")


if __name__ == "__main__":
    unittest.main(exit=False)
