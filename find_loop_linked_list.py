# Write a function that takes in the head of a Singly Linked List that contains a loop
# (in other words, the list's tail node points to some node in the list instead of the None (null) value).
# The function should return the node (the actual node - not just its value) from which the loop originates in constant
# space. Note that every node in the Singly Linked List has a "value" property storing its value as well as a "next"
# property pointing to the next node in the list.


def findLoop(head):
    turtle = head.next
    rabbit = head.next.next
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
    rabbit = head
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next
    return rabbit
