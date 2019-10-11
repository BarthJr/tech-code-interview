# https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: Node) -> Node:
    dct = dict()
    current = new_list = head
    while current:
        dct[current] = Node(current.val, current.next, current.random)
        current = current.next

    while new_list:
        dct[new_list].next = dct.get(new_list.next)
        dct[new_list].random = dct.get(new_list.random)
        new_list = new_list.next
    return dct.get(head)
