"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        first = second = head
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
        while first.next:
            first = first.next
            stack.append(first)
        first = head
        while len(stack) > 0:
            second = first.next
            first.next = stack.pop()
            first.next.next = second
            first = second
        first.next = None
