# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        tail = dummy
        dummy.next = head

        while True:
            i = 0
            lookahead = tail
            while i < k and lookahead.next:
                i += 1
                lookahead = lookahead.next
            if i != k:
                break
            prev, cur = lookahead.next, tail.next
            tail.next = lookahead
            tail = cur
            for i in range(k):
                nxt, cur.next = cur.next, prev
                prev, cur = cur, nxt

        return dummy.next
        
    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        lookahead = head
        i = 0
        while i < k - 1 and lookahead.next:
            i += 1
            lookahead = lookahead.next
        if i == k - 1:
            dummy.next = lookahead
            lookahead = lookahead.next

        cur = head
        while i == k - 1:
            prev = cur
            cur = cur.next
            head = prev
            for i in range(k - 1):
                nxt, cur.next = cur.next, prev
                prev, cur = cur, nxt
            i = 0
            if not lookahead:
                head.next = None
                break
            while i < k - 1 and lookahead.next:
                i += 1
                lookahead = lookahead.next
            if i == k - 1:
                head.next = lookahead
                lookahead = lookahead.next
            else:
                head.next = cur

        return dummy.next

class Solution1:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        i = 0
        while i < k and cur:
            i += 1
            cur = cur.next

        if i == k:
            cur =  self.reverseKGroup(cur, k)
            prev, cur = cur, head
            for i in range(k):
                nxt, cur.next = cur.next, prev
                prev, cur = cur, nxt
            head = prev

        return head

    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            if not head:
                return None
            lookahead = head
            i = 0
            while i < k - 1 and lookahead.next:
                i += 1
                lookahead = lookahead.next
            if i == k - 1:
                prev = head
                cur = head.next
                for i in range(k - 1):
                    nxt, cur.next = cur.next, prev
                    prev, cur = cur, nxt
                head.next = reverse(cur)
            else:
                return head

            return lookahead

        return reverse(head)
        
