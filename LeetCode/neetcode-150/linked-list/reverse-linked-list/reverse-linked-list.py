from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        nxt = head
        while nxt:
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
        return cur


        
