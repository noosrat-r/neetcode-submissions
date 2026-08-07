# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     leftHeight = self.height(root.left)
    #     rightHeight = self.height(root.right)

    #     if abs(leftHeight - rightHeight) > 1:
    #         return False

    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def height(self, curr):
    #     if not curr:
    #         return -1

    #     return 1 + max(self.height(curr.left), self.height(curr.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalancedRec(node):
            if not node:
                return (0, True)
            
            leftHeight, leftBalanced = isBalancedRec(node.left)
            rightHeight, rightBalanced = isBalancedRec(node.right)

            curBalanced = False if abs(leftHeight-rightHeight) > 1 else True
            return (1 + max(leftHeight, rightHeight), curBalanced and leftBalanced and rightBalanced)

        return isBalancedRec(root)[1]