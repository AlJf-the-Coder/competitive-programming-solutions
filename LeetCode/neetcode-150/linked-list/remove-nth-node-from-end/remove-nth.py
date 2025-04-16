# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        for i in range(n):
            cur = cur.next

        while cur:
            cur = cur.next
            prev = prev.next

        rm = prev.next
        prev.next = prev.next.next
        del rm
        return dummy.next

class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        n_nodes = 0
        while cur:
            cur = cur.next
            n_nodes += 1
        r = n_nodes - n
        if r == 0:
            nxt = head.next
            del head
            return nxt
        cur = head
        for i in range(r - 1):
            cur = cur.next
        remove = cur.next
        cur.next = cur.next.next
        del remove
        return head
