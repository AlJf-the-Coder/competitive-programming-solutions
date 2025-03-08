# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val > max(q.val, p.val):
                cur = cur.left
            elif cur.val < min(q.val, p.val):
                cur = cur.right
            else:
                return cur
            
        return None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root.val == p.val or root.val == q.val:
                return root
            else:
                if root.val > max(q.val, p.val):
                    return dfs(root.left)
                elif root.val < min(q.val, p.val):
                    return dfs(root.right)
                else:
                    return root
            
        return dfs(root)
