#   Write a function that takes in the heads of two Singly Linked Lists that are
#   in sorted order, respectively. The function should merge the lists in place
#   (i.e., it shouldn't create a brand new list) and return the head of the merged
#   list; the merged list should be in sorted order.
#
#   Each 'LinkedList' node has an integer 'value' as well as a 'next' node
#   pointing to the next node in the list or to 'None' if it's the tail of the list.
#
#   You can assume that the input linked lists will always have at least one node;
#   in other words, the heads will never be 'None'

"""
>>> mergedLinkedLists = mergeLinkedLists(LinkedList([2, 6, 7, 8]).head, LinkedList([1, 3, 4, 5, 9, 10]).head)
>>> LinkedList().print(mergedLinkedLists)
1->2->3->4->5->6->7->8->9->10
"""

from datastructs import LinkedList
from datastructs.linked_list import ListNode


def mergeLinkedLists(headOne: ListNode, headTwo: ListNode):
    p1 = headOne
    p2 = headTwo
    p1Prev = None

    while p1 and p2:
        if p1.val < p2.val:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1

    if not p1:
        p1Prev.next = p2

    return headOne if headOne.val < headTwo.val else headTwo
