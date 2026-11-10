class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_d = 0

        def findDiameter(node):
            if not node:
                return 0
            
            left = findDiameter(node.left)
            right = findDiameter(node.right)
            
            self.max_d = max(self.max_d, left + right)
            return 1 + max(left, right)
        
        findDiameter(root)
        return self.max_d