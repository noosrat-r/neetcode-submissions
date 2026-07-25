# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        remove = length - n
        print(remove)
        if remove == 0:
            temp = head
            head = head.next
            temp.next = None
            return head
            
        cur = head
        prev = head
        for _ in range(remove):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next
        cur.next = None

        return head