# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both trees are empty
        if not p and not q:
            return True
        
        # One tree is empty, the other is not
        if not p or not q:
            return False
        
        # Current nodes have different values
        if p.val != q.val:
            return False
        
        # Recursively check both subtrees
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        
        return left_same and right_same