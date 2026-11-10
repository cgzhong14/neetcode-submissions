# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(node):
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            currentDiameter = leftHeight + rightHeight
            self.maxDiameter = max(self.maxDiameter, currentDiameter)
            return 1 + max(leftHeight,rightHeight)

        dfs(root)
        return self.maxDiameter