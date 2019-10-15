# https://leetcode.com/problems/merge-k-sorted-lists/

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

"""
>>> list1 = LinkedList([1, 4, 5])
>>> list2 = LinkedList([1, 3, 4])
>>> list3 = LinkedList([2, 6])
>>> lists = [list1.head, list2.head, list3.head]
>>> merged_sorted_list = Solution().mergeKLists(lists)
>>> LinkedList().print(merged_sorted_list)
1->1->2->3->4->4->5->6
"""

import heapq
from typing import List
from datastructs import LinkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        for list in lists:
            while list:
                heapq.heappush(min_heap, list.val)
                list = list.next

        head = ListNode(-1)
        current = head
        while min_heap:
            current.next = ListNode(heapq.heappop(min_heap))
            current = current.next

        return head.next
