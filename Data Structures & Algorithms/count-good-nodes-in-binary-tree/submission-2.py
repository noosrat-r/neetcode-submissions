# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, root.val))        

        res = 0
        while queue:
            curr, maxVal = queue.popleft()

            if curr.val >= maxVal:
                res += 1
            
            if curr.left:
                queue.append((curr.left, max(maxVal, curr.left.val)))
            if curr.right:
                queue.append((curr.right, max(maxVal, curr.right.val)))
        
        return res
