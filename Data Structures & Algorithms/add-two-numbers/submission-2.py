# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        power = 0
        l1sum = 0
        while cur1:
            l1sum += pow(10, power) * cur1.val
            power += 1
            cur1 = cur1.next
        
        power = 0
        cur2 = l2
        l2sum = 0
        while cur2:
            l2sum += pow(10, power) * cur2.val
            power += 1
            cur2 = cur2.next
        
        sum = l1sum + l2sum
        if sum == 0:
            return ListNode(sum)
        
        base10div = 10
        dummy = ListNode(0)
        prev = dummy        
        while sum > 0:
            digit = sum % base10div
            digitNode = ListNode(digit)
            prev.next = digitNode
            prev = digitNode
            sum = sum // base10div
        
        return dummy.next