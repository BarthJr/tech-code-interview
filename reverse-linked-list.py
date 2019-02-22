# https://leetcode.com/problems/reverse-linked-list/
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head):
    previous = None
    current = head
    while current is not None:
        aux = current.next
        current.next = previous
        previous = current
        current = aux
    return previous
