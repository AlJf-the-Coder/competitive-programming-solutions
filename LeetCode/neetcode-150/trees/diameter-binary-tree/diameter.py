# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if not root:
                return -1
            l_depth = dfs(root.left)
            r_depth = dfs(root.right)
            self.diameter = max(self.diameter, l_depth + r_depth + 2)
            return max(l_depth, r_depth) + 1
        dfs(root)
        return self.diameter

class Solution1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_and_diameter(root):
            if not root:
                return -1, 0
            l_depth, l_diameter = depth_and_diameter(root.left)
            r_depth, r_diameter = depth_and_diameter(root.right)
            return max(l_depth, r_depth) + 1, max(l_diameter, r_diameter, r_depth + l_depth + 2)
        _, diameter = depth_and_diameter(root)
        return diameter
