# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = -1
        def dfs(i, head):
            nonlocal depth
            if not head:
                depth = max(depth, i)
            else:
                dfs(i + 1, head.left)
                dfs(i + 1, head.right)
        dfs(0, root)
        return depth

        
