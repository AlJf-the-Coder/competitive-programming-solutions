# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack.append(node.right)
                stack.append(node.left)
        return root

class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

