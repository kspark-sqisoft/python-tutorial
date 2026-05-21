"""
unittest 기본 — 파이썬 표준 라이브러리 테스트 프레임워크.
TestCase 클래스를 상속해 테스트 메서드를 정의하고,
다양한 어셋션(assertEqual, assertTrue 등)으로 결과를 검증한다.
"""

import unittest

# ──── 1. 테스트 대상 함수 ────

def add(a: int, b: int) -> int:
    """두 수를 더한다."""
    return a + b


def is_even(n: int) -> bool:
    """짝수이면 True를 반환한다."""
    return n % 2 == 0


def get_names() -> list[str]:
    """이름 목록을 반환한다."""
    return ["Alice", "Bob", "Charlie"]


# ──── 2. TestCase 클래스 ────

class TestMath(unittest.TestCase):
    """수학 유틸리티 함수 테스트."""

    def test_add(self):
        # 두 값이 같으면 통과
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(-1, 1), 0)

    def test_is_even_true(self):
        # 조건이 참이면 통과
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        # 조건이 거짓이면 통과
        self.assertFalse(is_even(3))

    def test_name_in_list(self):
        names = get_names()
        # 값이 컨테이너 안에 있으면 통과
        self.assertIn("Bob", names)
        self.assertNotIn("Dave", names)

    def test_division_by_zero(self):
        # 특정 예외가 발생하면 통과
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0


# ──── 3. 추가 어셋션 종류 ────

class TestAssertions(unittest.TestCase):
    """다양한 어셋션 메서드 예시."""

    def test_almost_equal(self):
        # 부동소수점 근사 비교 (소수점 7자리 기본)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)

    def test_is_instance(self):
        # 타입 검사
        self.assertIsInstance(add(1, 2), int)

    def test_is_none(self):
        value = None
        self.assertIsNone(value)

    def test_greater(self):
        self.assertGreater(add(3, 4), 5)


# ──── 4. 실행 ────

if __name__ == "__main__":
    # exit=False → 스크립트가 종료되지 않고 결과만 출력
    unittest.main(exit=False, verbosity=2)
