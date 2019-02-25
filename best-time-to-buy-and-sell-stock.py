# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import math
from unittest import TestCase


def maxProfit(prices):
    """
    :param prices: List[int]
    :return: int
    """

    min_price = math.inf
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


class Tests(TestCase):
    def test_with_better_profits_in_sequence(self):
        self.assertEqual(5, maxProfit([7, 1, 3, 4, 5, 6, 2]))

    def test_with_reverse_list(self):
        self.assertEqual(0, maxProfit([7, 6, 5, 4, 3, 2, 1]))

    def test_with_empty_list(self):
        self.assertEqual(0, maxProfit([]))
