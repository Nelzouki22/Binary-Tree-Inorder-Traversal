class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)      # 1. زر اليسار
            result.append(node.val) # 2. خذ الجذر
            inorder(node.right)     # 3. زر اليمين

        inorder(root)
        return result
