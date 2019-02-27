# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

from typing import List
from unittest import TestCase


def generate(numRows: int) -> List[List[int]]:
    result = []
    for num_row in range(numRows):
        row = [0 for _ in range(num_row + 1)]
        row[0] = row[-1] = 1
        for j in range(1, num_row):
            row[j] = result[num_row - 1][j] + result[num_row - 1][j - 1]
        result.append(row)
    return result


class TestGenerate(TestCase):
    def test_check_with_odd_number(self):
        self.assertEqual([
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ], generate(5))

    def test_check_with_even_number(self):
        self.assertEqual([
            [1],
            [1, 1],
        ], generate(2))

    def test_with_number_one_input(self):
        self.assertEqual([
            [1]
        ], generate(1))

    def test_with_number_zero_input(self):
        self.assertEqual([], generate(0))
