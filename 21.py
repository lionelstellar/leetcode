# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        t = ret
        while l1 != None or l2 != None:
            if l1 == None:
                t.next = l2
                return ret.next
            elif l2 == None:
                t.next = l1
                return ret.next
            else:
                if l1.val < l2.val:
                    t.next = l1
                    l1 = l1.next
                    t = t.next
                else:
                    t.next = l2
                    l2 = l2.next
                    t = t.next