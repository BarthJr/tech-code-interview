# Count the number of prime numbers less than a non-negative number, n.

from unittest import TestCase


def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    prime_numbers = [True] * n
    prime_numbers[0] = prime_numbers[1] = False
    i = 2
    while i * i < n:
        if prime_numbers[i]:
            for j in range(i * i, n, i):
                prime_numbers[j] = False
        i += 1
    return prime_numbers.count(True)


class TestCountPrimes(TestCase):
    def test_base_case(self):
        self.assertEqual(0, countPrimes(1))

    def test_simple_case(self):
        self.assertEqual(25, countPrimes(100))
