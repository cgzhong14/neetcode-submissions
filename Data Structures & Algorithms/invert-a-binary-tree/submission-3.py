                # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # for every node swap its children
        tmp = root
        def invert(root):
            if not root:
                return
            tmp1 = root.left
            tmp2 = root.right
            root.left = tmp2
            root.right = tmp1
            invert(root.left)
            invert(root.right)
        invert(root)
        return tmp


