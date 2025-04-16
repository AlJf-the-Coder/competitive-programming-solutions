class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -float('inf')
        def dfs(root):
            if not root:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            one_side = max(0, left_sum, right_sum)
            self.max_path = max(self.max_path, max(one_side, left_sum + right_sum) + root.val)
            return one_side + root.val
        dfs(root)
        return self.max_path

class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -float('inf')
        def dfs(root):
            if not root:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            self.max_path = max(self.max_path, left_sum + right_sum + root.val, right_sum + root.val, left_sum + root.val, root.val)
            return max(0, left_sum, right_sum) + root.val
        dfs(root)
        return self.max_path
