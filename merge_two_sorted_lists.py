# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

"""
>>> l1 = create_linked_list([1, 2, 4])
>>> print_linked_list(l1)
1->2->4
>>> l2 = create_linked_list([1, 3, 4])
>>> print_linked_list(l2)
1->3->4
>>> merged_linked_lists = merge_two_lists(l1, l2)
>>> print_linked_list(merged_linked_lists)
1->1->2->3->4->4
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(lst: List) -> ListNode:
    if lst:
        head = tail = ListNode(lst[0])
        for i in range(1, len(lst)):
            tail.next = ListNode(lst[i])
            tail = tail.next
        return head


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    head = tail = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next


def print_linked_list(linked_list):
    while linked_list:
        if linked_list.next:
            print(linked_list.val, end='->')
        else:
            print(linked_list.val)
        linked_list = linked_list.next
