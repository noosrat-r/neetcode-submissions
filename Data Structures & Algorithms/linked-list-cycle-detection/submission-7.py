# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        def hasCycleRecursive(slow, fast):
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
                        
            if fast is slow:
                return True
            return hasCycleRecursive(slow, fast)

        if not head:
            return False
        
        return hasCycleRecursive(head, head)