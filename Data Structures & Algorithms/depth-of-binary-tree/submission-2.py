# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        return self.findDepth(root,counter)

    def findDepth(self, root, counter):
        if not root:
            return counter
        counter+=1
        right = self.findDepth(root.left,counter)
        left = self.findDepth(root.right,counter)
        return max(right,left)
