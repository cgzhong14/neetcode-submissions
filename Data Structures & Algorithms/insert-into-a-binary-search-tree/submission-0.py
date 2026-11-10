class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        left = root.left
        right = root.right
        if root.val < val:
            if not right:
                root.right = TreeNode(val)
                return root
            else:
                self.insertIntoBST(root.right, val)
                return root
        if root.val > val:
            if not left:
                root.left = TreeNode(val)
                return root
            else:
                self.insertIntoBST(root.left, val)
                return root