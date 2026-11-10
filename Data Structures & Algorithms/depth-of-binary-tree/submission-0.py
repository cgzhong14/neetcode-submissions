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
        count = 1
        return self.findDepth(root,count)

    def findDepth(self, root, count):
        if not root:
            return count
        if not root.left and not root.right:
            return count
        count += 1
        return max(self.findDepth(root.left, count), self.findDepth(root.right, count))