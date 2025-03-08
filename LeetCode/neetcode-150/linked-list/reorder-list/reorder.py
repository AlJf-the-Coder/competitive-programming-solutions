# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head.next
        half_2 = head
        while cur and cur.next:
            cur = cur.next.next
            half_2 = half_2.next

        cur = half_2.next
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        half_2.next = None
        half_2 = prev

        cur = head
        while half_2:
            nxt = cur.next
            cur.next = half_2
            half_2 = half_2.next
            cur.next.next = nxt
            cur = nxt


        
