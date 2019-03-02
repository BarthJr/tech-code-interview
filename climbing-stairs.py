# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.
from unittest import TestCase


def climbStairs(n: int) -> int:
    memo = [0] * (n + 1)
    return _climb_stairs(0, n, memo)


def _climb_stairs(i, n, memo):
    if i > n:
        return 0
    elif i == n:
        return 1
    elif memo[i] > 0:
        return memo[i]
    memo[i] = _climb_stairs(i + 1, n, memo) + _climb_stairs(i + 2, n, memo)
    return memo[i]


class TestClimbStairs(TestCase):
    def test_should_return_1_given_0(self):
        self.assertEqual(1, climbStairs(0))

    def test_should_return_2_given_2(self):
        self.assertEqual(2, climbStairs(2))

    def test_should_return_3_given_3(self):
        self.assertEqual(3, climbStairs(3))

    def test_should_return_8_given_5(self):
        self.assertEqual(8, climbStairs(5))
