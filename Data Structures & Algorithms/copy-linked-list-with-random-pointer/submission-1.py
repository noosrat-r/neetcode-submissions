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
        oldToNewNode = {None:None}

        cur = head
        while cur:
            newNode = Node(cur.val)
            oldToNewNode[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToNewNode[cur]
            copy.next = oldToNewNode[cur.next]
            copy.random = oldToNewNode[cur.random]
            cur = cur.next
        
        return oldToNewNode[head]