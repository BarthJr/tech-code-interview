# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


from unittest import TestCase


def strStr(haystack: str, needle: str) -> int:
    diff = len(haystack) - len(needle) + 1
    for i in range(diff):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1


class TestStrStr(TestCase):
    def test_with_empty_haystack_and_needle(self):
        haystack = ''
        needle = ''
        self.assertEqual(0, strStr(haystack, needle))

    def test_only_with_empty_haystack(self):
        haystack = ''
        needle = 'a'
        self.assertEqual(-1, strStr(haystack, needle))

    def test_only_with_empty_needle(self):
        haystack = 'a'
        needle = ''
        self.assertEqual(0, strStr(haystack, needle))

    def test_with_same_haystack_and_needle(self):
        haystack = 'a'
        needle = 'a'
        self.assertEqual(0, strStr(haystack, needle))

    def test_with_needle_in_haystack(self):
        haystack = 'banana'
        needle = 'ana'
        self.assertEqual(1, strStr(haystack, needle))

    def test_with_needle_not_in_haystack(self):
        haystack = 'banana'
        needle = 'cana'
        self.assertEqual(-1, strStr(haystack, needle))
