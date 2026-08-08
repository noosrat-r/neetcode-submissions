# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            curLevel = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node:
                    curLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curLevel:
                res.append(curLevel)
        return res