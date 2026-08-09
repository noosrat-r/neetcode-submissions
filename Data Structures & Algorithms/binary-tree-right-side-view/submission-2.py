# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []
        while queue:
            length = len(queue)
            last = None
            for _ in range(length):
                last = queue.popleft()
                if last.left:
                    queue.append(last.left)
                if last.right:
                    queue.append(last.right)
            
            res.append(last.val)
        
        return res