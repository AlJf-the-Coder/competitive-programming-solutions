# Definition for a Node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {None: None}

        def copy(cur):
            if cur:
                new_cur = Node(cur.val, cur.next, cur.random)
                new_nodes[cur] = new_cur
                new_cur.next = copy(cur.next)
                new_cur.random = new_nodes[new_cur.random]
                return new_cur
            return None
        
        return copy(head)

class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_nodes = {}
        cur = head
        while cur:
            new_nodes[cur] = Node(cur.val, cur.next, cur.random)
            cur = cur.next
        for node in new_nodes.values():
            if node.next:
                node.next = new_nodes[node.next]
            if node.random:
                node.random = new_nodes[node.random]
        return new_nodes[head]


