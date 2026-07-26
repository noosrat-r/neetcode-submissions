"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        cur = head
        while cur:
            newCopy = Node(cur.val)
            newCopy.next = cur.next
            cur.next = newCopy
            cur = cur.next.next

        cur = head
        while cur:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            cur = copy.next

        newHead = head.next
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        
        return newHead


