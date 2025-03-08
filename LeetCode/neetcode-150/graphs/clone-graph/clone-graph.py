"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        addresses = {}
        q = deque([node])
        addresses[node.val] = Node(node.val)
        while q:
            cur = q.popleft()
            print(cur.val, [n.val for n in cur.neighbors])
            for neighbor in cur.neighbors:
                if neighbor.val not in addresses:
                    q.append(neighbor)
                    addresses[neighbor.val] = Node(neighbor.val)
                addresses[cur.val].neighbors.append(addresses[neighbor.val])
        return addresses[node.val]

class Solution1:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        addresses = {}
        def dfs(node):
            new_node = Node(node.val)
            addresses[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val not in addresses:
                    addresses[neighbor.val] = dfs(neighbor)
                new_node.neighbors.append(addresses[neighbor.val])
            return new_node
        return dfs(node) if node else None
