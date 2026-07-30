# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # # leftSum = 1 + self.maxDepth(root.left)
        # # rightSum = 1 + self.maxDepth(root.right)
        # return 1 + max(leftSum, rightSum)

        # if not root:
        #     return 0
        
        # queue = deque([root])
        # level = 0
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     level += 1
        
        # return level

        if not root:
            return 0
            
        stack = [(root, 1)]

        res = 0
        while stack:
            print("***")
            print(stack)
            node, depth = stack.pop()
            print(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

            print(depth)
            res = max(res, depth)
        
        return res
            