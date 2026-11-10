# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def countDepth(counter, tree):
            if not tree:
                return counter
            counter+=1
            leftCounter = countDepth(counter , tree.left)
            rightCounter = countDepth(counter, tree.right)
            return max(rightCounter, leftCounter)

        if not root:
            return 0
        
        count = 0
        return countDepth(count, root)
