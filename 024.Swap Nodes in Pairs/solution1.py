# Definition for singly-linked list.
from utils.ListNode import create_linklist, display_linklist, ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        new_head = head.next
        cur = new_head.next
        new_head.next = head
        head.next = cur
        pre = head

        while cur != None and cur.next != None:
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next

        return new_head




sol = Solution()
val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = create_linklist(val_list)
new_head = sol.swapPairs(head)
display_linklist(new_head)



