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
        ptr1 = head

        dummy2 = Node(0)
        prev2 = dummy2
        nodeMap = {}
        while ptr1:
            new2 = Node(ptr1.val)
            nodeMap[ptr1] = new2
            prev2.next = new2
            prev2 = new2
            ptr1 = ptr1.next

        ptr2 = dummy2
        ptr1 = head
        while ptr1:
            newRandom2 = nodeMap.get(ptr1.random, None)
            ptr2.next.random = newRandom2

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return dummy2.next
