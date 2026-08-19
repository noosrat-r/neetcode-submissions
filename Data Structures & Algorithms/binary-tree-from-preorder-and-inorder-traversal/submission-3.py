# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {value:index for index,value in enumerate(inorder)}
        preorderIndex = 0
        def dfs(l, r):
            nonlocal preorderIndex
            if l > r:
                return None
            
            val = preorder[preorderIndex]
            node = TreeNode(val)
            preorderIndex += 1
            inorderIndex = inorderMap[val]
            node.left = dfs(l, inorderIndex - 1)
            node.right = dfs(inorderIndex + 1, r)
            return node
        
        return dfs(0, len(inorder) - 1)

