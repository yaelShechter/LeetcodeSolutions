"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            value1 = value2 = 0
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next

            value = value1 + value2 + carry
            curr.next = ListNode(value % 10)
            curr = curr.next
            carry = value // 10

        return head.next
      
      
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
