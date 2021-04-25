# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1=l1
        p2=l2
        l3=ListNode(None)
        t=l3
        c=0
        while p1 or p2 or c:
            sum = p1.val + p2.val + c
            val = sum % 10
            c = sum // 10
            if p1 is not None:
                p1=p1.next
            if p2 is not None:
                p2=p2.next
            t.next = ListNode(val)
            t = t.next
        return l3

