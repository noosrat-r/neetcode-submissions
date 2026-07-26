# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        remainder = 0
        dummy = ListNode(0)
        prev = dummy
        while cur1 or cur2:
            sum = 0
            if cur1:
                sum += cur1.val
            if cur2:
                sum += cur2.val
            
            sum += remainder
            digit = sum % 10
            newDigitNode = ListNode(digit)
            prev.next = newDigitNode
            prev = newDigitNode
            remainder = sum // 10

            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next
        
        if remainder == 1:
            prev.next = ListNode(remainder)
        
        return dummy.next