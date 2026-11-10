# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node, count):
            if not node:
                return count
            count+=1
            return max(findDepth(node.left,count), findDepth(node.right,count))
        result = findDepth(root, 0)
        return result