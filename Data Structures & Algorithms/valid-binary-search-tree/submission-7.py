# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, rangeMin, rangeMax):
            if not node:
                return True
            if node.val <= rangeMin or node.val >= rangeMax:
                return False
            
            return dfs(node.left, rangeMin, node.val) and dfs(node.right, node.val, rangeMax)
        
        return dfs(root, float('-inf'), float('inf'))

