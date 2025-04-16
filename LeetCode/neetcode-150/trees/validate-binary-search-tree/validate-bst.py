# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, bound_l, bound_r):
            if not root:
                return True
            return bound_l < root.val < bound_r and dfs(root.left, bound_l, root.val) and dfs(root.right, root.val, bound_r)
        return dfs(root, -float('infinity'), float('infinity'))

class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def traverse(root):
            if not root:
                return True
            if not traverse(root.left):
                return False
            if self.prev is not None:
                if root.val <= self.prev:
                    return False
            self.prev = root.val
            return traverse(root.right)
        return traverse(root)

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, bound_l, bound_r):
            if not root:
                return True
            res = True
            if bound_r is None and bound_l is not None:
                res = root.val > bound_l
            elif bound_l is None and bound_r is not None:
                res = root.val < bound_r
            elif bound_l is not None and bound_r is not None:
                res = bound_l < root.val < bound_r
            return res and dfs(root.left, bound_l, root.val) and dfs(root.right, root.val, bound_r)
        return dfs(root, None, None)
