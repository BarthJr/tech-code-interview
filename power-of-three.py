# Given an integer, write a function to determine if it is a power of three.

from math import log
from unittest import TestCase


def isPowerOfThree(n: int) -> bool:
    return n > 0 and abs(log(n, 3) - round(log(n, 3))) < 1e-10


class TestIsPowerOfThree(TestCase):
    def test_limit(self):
        self.assertEqual(False, isPowerOfThree(0))

    def test_simple_true_case(self):
        self.assertEqual(True, isPowerOfThree(27))

    def test_simple_false_case(self):
        self.assertEqual(False, isPowerOfThree(45))

    def test_with_large_input_returning_false(self):
        self.assertEqual(False, isPowerOfThree(1_162_261_466))

    def test_with_large_input_returning_true(self):
        self.assertEqual(True, isPowerOfThree(1_162_261_467))

