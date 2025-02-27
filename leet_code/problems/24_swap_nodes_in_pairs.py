"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def swapPairs(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Base case
    if not head or not head.next:
        return head

    # Store the nodes you'll need
    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second
