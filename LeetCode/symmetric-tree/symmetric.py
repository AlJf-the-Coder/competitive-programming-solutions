class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if not right and not left:
                return True
            if not right or not left:
                return False
            return left.val == right.val and compare(left.left, right.right) and compare(left.right, right.left)
        return not root or compare(root.left, root.right)
