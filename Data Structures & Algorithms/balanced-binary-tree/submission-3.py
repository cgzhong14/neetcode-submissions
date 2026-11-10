# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkHeight(node):
            # Base case: empty tree has height 0 and is balanced
            if not node:
                return 0
            
            # Recursively check left subtree
            left_height = checkHeight(node.left)
            if left_height == -1:  # Left subtree is not balanced
                return -1
            
            # Recursively check right subtree
            right_height = checkHeight(node.right)
            if right_height == -1:  # Right subtree is not balanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current node
            return max(left_height, right_height) + 1
        
        return checkHeight(root) != -1