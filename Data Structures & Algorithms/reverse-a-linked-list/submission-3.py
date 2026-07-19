# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # newHead = None

        # ptr = head
        # while ptr != None:
        #     newNode = ListNode(ptr.val)
        #     if newHead != None:
        #         newNode.next = newHead
        #     newHead = newNode
        #     ptr = ptr.next

        # return newHead
        if not head:
            return head

        oldHead = head
        while oldHead.next != None:
            swap = oldHead.next
            oldHead.next = swap.next
            swap.next = head
            head = swap
        
        return head

