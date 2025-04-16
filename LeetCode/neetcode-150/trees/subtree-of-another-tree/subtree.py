# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(root, root2):
            if not root and not root2:
                return True
            if not root or not root2:
                return False
            return root.val == root2.val and isSame(root.left, root2.left) and isSame(root.right, root2.right)

        if not root and subRoot:
            return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
