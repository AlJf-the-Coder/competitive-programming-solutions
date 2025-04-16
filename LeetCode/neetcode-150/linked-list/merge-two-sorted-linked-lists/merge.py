# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return head.next

class Solution1(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        add = list2
        prev = None
        cur = list1
        while add != None:
            next = add.next
            if list1 == None:
                list1 = add
                list1.next = None
            else:
                while cur != None and cur.val < add.val:
                    prev = cur
                    cur = cur.next
                if prev == None:
                    add.next = list1
                    list1 = add
                else:
                    prev.next = add
                    add.next = cur
            cur = add
            add = next
        return list1

