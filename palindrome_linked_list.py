# Given a singly linked list, determine if it is a palindrome.

from typing import List
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_palindrome(head: ListNode) -> bool:
    reversed_linked_list = None
    current = fast = head
    while fast and fast.next:
        fast = fast.next.next
        current, reversed_linked_list, reversed_linked_list.next = current.next, current, reversed_linked_list
    if fast:
        current = current.next
    while reversed_linked_list and reversed_linked_list.val == current.val:
        current = current.next
        reversed_linked_list = reversed_linked_list.next
    return not reversed_linked_list


def create_linked_list(lst: List) -> ListNode:
    if lst:
        head = tail = ListNode(lst[0])
        for i in range(1, len(lst)):
            tail.next = ListNode(lst[i])
            tail = tail.next
        return head


class TestIsPalindrome(TestCase):
    def test_with_empty_linked_list_should_return_true(self):
        linked_list = create_linked_list([])
        self.assertTrue(is_palindrome(linked_list))

    def test_with_one_value_in_linked_list_should_return_true(self):
        linked_list = create_linked_list([1])
        self.assertTrue(is_palindrome(linked_list))

    def test_with_even_palindrome_linked_list(self):
        linked_list = create_linked_list([1, 2, 2, 1])
        self.assertTrue(is_palindrome(linked_list))

    def test_with_odd_palindrome_linked_list(self):
        linked_list = create_linked_list([1, 2, 2, 1])
        self.assertTrue(is_palindrome(linked_list))

    def test_with_even_not_palindrome_linked_list(self):
        linked_list = create_linked_list([1, 2, 3])
        self.assertFalse(is_palindrome(linked_list))

    def test_with_odd_not_palindrome_linked_list(self):
        linked_list = create_linked_list([1, 2, 3])
        self.assertFalse(is_palindrome(linked_list))
