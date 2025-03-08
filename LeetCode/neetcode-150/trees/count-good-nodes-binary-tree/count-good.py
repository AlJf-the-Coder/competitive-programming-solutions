# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_count = 0
        def dfs(mx, node):
            if not node:
                return
            if mx <= node.val:
                self.good_count += 1
            new_mx = max(mx, node.val)
            dfs(new_mx, node.left)
            dfs(new_mx, node.right)
        if root:
            dfs(root.val, root)
        return self.good_count
