# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

"""
>>> letter_combinations('23')
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
>>> letter_combinations('2')
['a', 'b', 'c']
>>> letter_combinations('')
[]

"""
from itertools import product
from typing import List


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    map_numbers = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }
    res = (map_numbers[digit] for digit in digits)
    return [''.join(i) for i in list(product(*res))]
