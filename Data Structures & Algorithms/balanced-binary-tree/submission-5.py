class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def findHeight(node, height):
            if not node:
                return height
            height += 1
            leftHeight = findHeight(node.left, height)
            rightHeight = findHeight(node.right, height)
            return max(leftHeight, rightHeight)
            
        if abs(findHeight(root.left, 0) - findHeight(root.right, 0)) > 1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)