# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        counter = 0
        def depth(node, counter):
            if not node:
                return counter
            counter+=1
            return max(depth(node.left,counter),depth(node.right,counter))
        return depth(root,counter)
        