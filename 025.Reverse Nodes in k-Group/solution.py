# Definition for singly-linked list.
from utils.ListNode import create_linklist, display_linklist, ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def chopKNode(head: ListNode, k: int):
            cur = head
            tail = head
            for i in range(k - 1):
                # put k - 1 nodes to the head
                if cur.next != None:
                    new_head = cur.next
                    cur.next = cur.next.next
                    new_head.next = head
                    head = new_head
                else:
                    # if list contains less than k node, reverse it again
                    cur = head
                    tail = head
                    for i in range(k - 1):
                        if cur.next != None:
                            new_head = cur.next
                            cur.next = cur.next.next
                            new_head.next = head
                            head = new_head
                    return head, tail

            return head, tail

        res_head, res_tail = chopKNode(head, k)

        while res_tail.next != None:
            tmp_head, tmp_tail = chopKNode(res_tail.next, k)
            res_tail.next = tmp_head
            res_tail = tmp_tail

        return res_head




sol = Solution()
val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = create_linklist(val_list)
display_linklist(head)

new_head = sol.reverseKGroup(head, 4)
display_linklist(new_head)



