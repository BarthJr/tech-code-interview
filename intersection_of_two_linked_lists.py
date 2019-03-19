# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Write a program to find the node at which the intersection of two singly linked lists begins.
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

"""
>>> lst_a = [4, 1, 8, 4, 5]
>>> lst_b = [5, 0, 1, 8, 4, 5]
>>> LLA, LLB = create_linked_lists_and_intersection_between_then(8, 2, 3, lst_a, lst_b)
>>> print_linked_list(LLA)
4->1->8->4->5
>>> print_linked_list(LLB)
5->0->1->8->4->5
>>> intersection_node = getIntersectionNode(LLA, LLB)
>>> intersection_node.val
8

>>> lst_a = [0, 9, 1, 2, 4]
>>> lst_b = [3, 2, 4]
>>> LLA, LLB = create_linked_lists_and_intersection_between_then(2, 3, 1, lst_a, lst_b)
>>> print_linked_list(LLA)
0->9->1->2->4
>>> print_linked_list(LLB)
3->2->4
>>> intersection_node = getIntersectionNode(LLA, LLB)
>>> intersection_node.val
2
"""

from typing import List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    nodeA, nodeB = headA, headB
    while nodeA is not nodeB:
        nodeA = headB if not nodeA else nodeA.next
        nodeB = headA if not nodeB else nodeB.next
    return nodeB


def create_linked_lists_and_intersection_between_then(intersectVal: int, skipA: int, skipB: int, lstA: List,
                                                      lstB: List) -> ListNode:
    linked_list_a = _create_linked_list(lstA)
    linked_list_b = _create_linked_list(lstB)
    _create_intersection_between_linked_lists(intersectVal, skipA, skipB, linked_list_a, linked_list_b)
    return linked_list_a, linked_list_b


def _create_linked_list(lst: List) -> ListNode:
    if lst:
        head = tail = ListNode(lst[0])
        for i in range(1, len(lst)):
            tail.next = ListNode(lst[i])
            tail = tail.next
        return head


def _create_intersection_between_linked_lists(intersectVal: int, skipA: int, skipB: int, LLA: ListNode,
                                              LLB: ListNode) -> ListNode:
    nodeA, nodeB = LLA, LLB
    for i in range(skipA):
        nodeA = nodeA.next

    for i in range(skipB - 1):
        nodeB = nodeB.next
    nodeB.next = nodeA


def print_linked_list(linked_list):
    while linked_list:
        if linked_list.next:
            print(linked_list.val, end='->')
        else:
            print(linked_list.val)
        linked_list = linked_list.next
