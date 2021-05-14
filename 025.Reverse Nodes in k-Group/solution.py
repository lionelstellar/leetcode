# Definition for singly-linked list.
from utils.ListNode import create_linklist, display_linklist, ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head

        for _ in range(k - 1):
            new_head = cur.next
            cur.next = cur.next.next
            new_head.next = head
            head = new_head
            display_linklist(head)

        ret_head = head
        tail =

        return head

        def chopKNode(head: ListNode, k: int):
            cur = head
            for _ in range(k - 1):
                if cur.next != None:
                    new_head = cur.next
                    cur.next = cur.next.next
                    new_head.next = head
                    head = new_head
                    display_linklist(head)



sol = Solution()
val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
head = create_linklist(val_list)
display_linklist(head)

new_head = sol.reverseKGroup(head, 4)
display_linklist(new_head)



