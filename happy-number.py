# https://leetcode.com/problems/happy-number/
from unittest import TestCase


def isHappy(n: int) -> bool:
    memo = set()
    while n not in memo:
        memo.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1


class TestIsHappy(TestCase):
    def test_with_happy_number(self):
        self.assertEqual(True, isHappy(78999))

    def test_with_unhappy_number(self):
        self.assertEqual(False, isHappy(4))
