# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
from unittest import TestCase


def isPalindrome(s: str) -> bool:
    cleaned_s = [c.lower() for c in s if c.isalnum()]
    return cleaned_s == list(reversed(cleaned_s))


class TestIsPalindrome(TestCase):
    def test_with_empty_string(self):
        self.assertTrue(isPalindrome(''))

    def test_with_one_character(self):
        self.assertTrue(isPalindrome('a'))

    def test_with_valid_palindrome(self):
        self.assertTrue(isPalindrome('A man, a plan, a canal: Panama'))

    def test_with_not_valid_palindrome(self):
        self.assertFalse(isPalindrome('race a car'))
