# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(root):
            if not self.is_balanced or not root:
                return -1
            l_depth = dfs(root.left)
            r_depth = dfs(root.right)
            self.is_balanced = self.is_balanced and abs(l_depth - r_depth) <= 1
            return max(l_depth, r_depth) + 1
        dfs(root)
        return self.is_balanced
        
class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced_and_depth(root):
            if not root:
                return -1, True
            l_depth, l_bal = balanced_and_depth(root.left)
            r_depth, r_bal = balanced_and_depth(root.right)
            return max(l_depth, r_depth) + 1, l_bal and r_bal and abs(l_depth - r_depth) <= 1
        _, balanced = balanced_and_depth(root)
        return balanced
        
