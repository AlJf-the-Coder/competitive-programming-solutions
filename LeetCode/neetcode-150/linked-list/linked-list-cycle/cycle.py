class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        node = head
        while node and node not in seen:
            seen.add(node)
            node = node.next
        return bool(node)
