# Write a function that takes in the head of a Singly Linked List and
# an integer k (assume that the list has at least k nodes).
# The function should remove the kth node from the end of the list.
# Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next" property
# pointing to the next node in the list or None (null) if it is the tail of the list.


def removeKthNodeFromEnd(head, k):
    count = 1
    first = head
    second = head
    while count <= k:
        count += 1
        second = second.next
    if not second:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next:
        first = first.next
        second = second.next
    first.next = first.next.next
