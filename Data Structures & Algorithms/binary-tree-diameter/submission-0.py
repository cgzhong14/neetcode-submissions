# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # Get height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter if path through current node is longer
            # The path length through this node is left_height + right_height
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of current subtree
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter