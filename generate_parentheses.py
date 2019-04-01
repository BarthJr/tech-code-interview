# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
"""
>>> generate_parentheses(0)
['']
>>> generate_parentheses(3)
['((()))', '(()())', '(())()', '()(())', '()()()']
"""
from typing import List


def generate_parentheses(num_of_pairs_parentheses: int) -> List[str]:
    result = []
    backtracking(num_of_pairs_parentheses, result)
    return result


def backtracking(n, result, left=0, right=0, parentheses=''):
    if len(parentheses) == n * 2:
        return result.append(parentheses)
    if left < n:
        backtracking(n, result, left + 1, right, parentheses + '(')
    if right < left:
        backtracking(n, result, left, right + 1, parentheses + ')')
