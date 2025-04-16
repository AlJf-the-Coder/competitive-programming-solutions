# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        k = len(lists)
        if k == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[: k // 2])
        l2 = self.mergeKLists(lists[k // 2:])
        return self.mergeTwoLists(l1, l2)

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        for i in range(len(lists)):
            head = self.mergeTwoLists(head, lists[i])
        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 or list2
        return head.next

class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = res = ListNode()
        lists = [l for l in lists if l]
        n = len(lists)
        while n > 0:
            min_ind = 0
            for i in range(n):
                if lists[i].val < lists[min_ind].val:
                    min_ind = i
            res.next = lists[min_ind]
            res = res.next
            lists[min_ind] = lists[min_ind].next
            if not lists[min_ind]:
                lists.pop(min_ind)
                n -= 1
        res.next = None
        return head.next
