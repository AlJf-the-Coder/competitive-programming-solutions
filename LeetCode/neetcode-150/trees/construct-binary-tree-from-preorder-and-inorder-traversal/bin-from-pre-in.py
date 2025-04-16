# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {inorder[i]: i for i in range(len(inorder))}
        node_map = {0: TreeNode(preorder[0])}
        root_inorder = inorder_indices[preorder[0]]
        stack = [(node_map[0], root_inorder)]
        for r in range(1, len(preorder)):
            node, r_i = stack[-1]
            if r not in node_map:
                node_map[r] = TreeNode(preorder[r])
            ind = inorder_indices[preorder[r]]
            if ind < r_i:
                node.left = node_map[r]
                stack.append((node.left, ind))
            else:
                node, r_i = stack.pop()
                while stack and ind - stack[-1][-1] > 0:
                    node, r_i = stack.pop()
                node.right = node_map[r]
                stack.append((node.right, ind))

        return node_map[0]

class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {inorder[i]: i for i in range(len(inorder))}
        node_map = {0: TreeNode(preorder[0])}
        p = 0

        def dfs(l, r):
            nonlocal p
            if r - l < 0 or p >= len(preorder):
                return None
            m = p
            if m not in node_map:
                node_map[m] = TreeNode(preorder[m])
            node = node_map[m]
            p += 1
            node.left = dfs(l, inorder_indices[preorder[m]] - 1)
            node.right = dfs(inorder_indices[preorder[m]] + 1, r)
            return node

        dfs(0, len(preorder) - 1)
        return node_map[0]

class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_map = {preorder[0]: TreeNode(preorder[0])}
        root_inorder = inorder.index(preorder[0])
        stack = [(node_map[preorder[0]], root_inorder)]
        def traverse(r):
            if r >= len(preorder):
                return 
            node, r_i = stack[-1]
            if preorder[r] not in node_map:
                node_map[preorder[r]] = TreeNode(preorder[r])
            for i in range(r_i - 1, -1, -1):
                if preorder[r] == inorder[i]:
                    node.left = node_map[preorder[r]]
                    stack.append((node.left, i))
                    traverse(r + 1)
                    break
                if inorder[i] in node_map:
                    break
            if node.left:
                return

            while not node.right:
                node, r_i = stack[-1]
                for i in range(r_i + 1, len(preorder)):
                    if preorder[r] == inorder[i]:
                        node.right = node_map[preorder[r]]
                        stack.pop()
                        stack.append((node.right, i))
                        traverse(r + 1)
                        break
                    if inorder[i] in node_map:
                        stack.pop()
                        break           

        traverse(1)
        return node_map[preorder[0]]
