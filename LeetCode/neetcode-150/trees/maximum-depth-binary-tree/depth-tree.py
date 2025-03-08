# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

class Solution1:
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


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)  
            return max(left, right) + 1
        
        
