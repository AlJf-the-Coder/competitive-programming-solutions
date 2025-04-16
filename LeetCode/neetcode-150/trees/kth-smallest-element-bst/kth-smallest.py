# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 1
        def traverse(root):
            if not root:
                return None
            left_val = traverse(root.left)
            if left_val is not None:
                return left_val
            if self.index == k:
                return root.val
            self.index += 1
            return traverse(root.right)
        return traverse(root)

