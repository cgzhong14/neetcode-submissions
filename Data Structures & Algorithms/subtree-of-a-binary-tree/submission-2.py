# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Empty subRoot is always a subtree
        if not subRoot:
            return True
        
        # Empty root but non-empty subRoot
        if not root:
            return False
        
        # Check if trees match at current node
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both null
        if not p and not q:
            return True
        
        # One is null or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Check both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
