# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            # Base case: null node has height 0
            if not node:
                return 0
            
            # Get the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The diameter passing through this node is the sum of 
            # left and right heights (number of edges)
            current_diameter = left_height + right_height
            
            # Update global maximum diameter
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return height of this subtree (add 1 for edge to parent)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter