# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEquivalent(p, q):
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return isEquivalent(p.left, q.left) and isEquivalent(p.right, q.right)
            
            return False

        if not root and not subRoot:
            return True
        if root and not subRoot or not root and subRoot:
            return False

        leftIsSubtree = self.isSubtree(root.left, subRoot)
        rightIsSubtree = self.isSubtree(root.right, subRoot)

        return leftIsSubtree or rightIsSubtree or isEquivalent(root, subRoot)