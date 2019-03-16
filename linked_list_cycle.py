# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
# If pos is -1, then there is no cycle in the linked list.


from typing import List
from unittest import TestCase


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(lst: List, pos: int) -> ListNode:
    if lst:
        head = tail = ListNode(lst[0])
        for i in range(1, len(lst)):
            tail.next = ListNode(lst[i])
            tail = tail.next

        if pos > -1:
            index = head
            for i in range(pos):
                index = index.next
            tail.next = index
        return head


def has_cycle(head: ListNode) -> bool:
    if head:
        seen = set()
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
            head = head.next
    return False


class TestHasCycle(TestCase):
    def test_cycle_in_first_element(self):
        lst = [3, 2, 0, -4]
        linked_list = create_linked_list(lst, 0)
        self.assertTrue(has_cycle(linked_list))

    def test_cycle_in_last_element(self):
        lst = [3, 2, 0, -4]
        linked_list = create_linked_list(lst, len(lst) - 1)
        self.assertTrue(has_cycle(linked_list))

    def test_cycle_with_linked_list_of_size_1(self):
        lst = [2]
        linked_list = create_linked_list(lst, len(lst) - 1)
        self.assertTrue(has_cycle(linked_list))

    def test_without_cycle_with_linked_list_of_size_1(self):
        lst = [2]
        linked_list = create_linked_list(lst, -1)
        self.assertFalse(has_cycle(linked_list))

    def test_without_cycle_with_linked_list_of_size_2(self):
        lst = [1, 4]
        linked_list = create_linked_list(lst, -1)
        self.assertFalse(has_cycle(linked_list))

    def test_with_empty_linked_list(self):
        lst = []
        linked_list = create_linked_list(lst, -1)
        self.assertFalse(has_cycle(linked_list))
