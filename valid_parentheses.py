# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#     1. Open brackets must be closed by the same type of brackets.
#     2. Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

from unittest import TestCase


def isValid(s: str) -> bool:
    stack = []
    reversed_brackets = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    for bracket in s:
        if bracket in '([{':
            stack.append(bracket)
        elif stack and bracket == reversed_brackets[stack[-1]]:
            stack.pop()
        else:
            return False
    return not stack


class TestIsValid(TestCase):
    def test_empty_input(self):
        self.assertTrue(isValid(''))

    def test_checks_all_types_of_valid_brackets(self):
        self.assertTrue(isValid('()[]{}'))

    def test_checks_if_open_with_one_type_of_bracket_and_close_with_other_return_false(self):
        self.assertFalse(isValid('(]'))

    def test_checks_if_multiple_brackets_are_closed_the_wrong_order(self):
        self.assertFalse(isValid('([)]'))

    def test_checks_if_multiple_brackets_are_closed_the_right_order(self):
        self.assertTrue(isValid('{[]}'))

    def test_checks_if_there_is_one_bracket_closed_the_wrong_way(self):
        self.assertFalse(isValid('[]}()'))

    def test_checks_if_start_with_closed_type_of_bracket_return_false(self):
        self.assertFalse(isValid('}[]'))
