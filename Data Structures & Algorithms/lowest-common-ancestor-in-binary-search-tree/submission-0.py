# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visitedP = []
        visitedQ = []

        curr = root
        while(True):
            visitedP.append(curr)

            if curr.val == p.val:
                break

            if curr.val < p.val:
                curr = curr.right
            elif curr.val > p.val:
                curr = curr.left
        
        curr = root
        while(True):
            visitedQ.append(curr)

            if curr.val == q.val:
                break

            if curr.val < q.val:
                curr = curr.right
            elif curr.val > q.val:
                curr = curr.left

        lca = root
        for a,b in zip(visitedP, visitedQ):
            if a == b:
                lca = a
            else:
                break
        return lca