# Binary Tree Inorder Traversal (Python)

A simple Python project to demonstrate **inorder traversal** of a binary tree. This project is perfect for beginners who want to understand how binary trees work and how to traverse them.

---

## Features
- Performs **inorder traversal** (Left → Root → Right)
- Works with any binary tree structure
- Simple and easy-to-understand Python code
- Includes examples for quick testing

---

## Example Code

```python
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    helper(root)
    return res

# Example usage:
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root))  # Output: [1, 3, 2]
