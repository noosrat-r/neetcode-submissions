# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        visitedInfo = {None:(0,0)}
        
        while stack:
            node = stack[-1]

            if node.right and node.right not in visitedInfo:
                stack.append(node.right)
            elif node.left and node.left not in visitedInfo:
                stack.append(node.left)
            else:
                poppedNode = stack.pop()

                leftHeight, leftDiameter = visitedInfo[poppedNode.right]
                rightHeight, rightDiameter = visitedInfo[poppedNode.left]

                visitedInfo[poppedNode] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
            
        return visitedInfo[root][1]