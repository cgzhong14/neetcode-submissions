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

        def findDepth(root,count):
            if not root:
                return count
            count+=1
            return max(findDepth(root.left,count),findDepth(root.right,count) )
        count = findDepth(root,0)
        return count