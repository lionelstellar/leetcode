# Definition for singly-linked list.
from utils.ListNode import create_linklist, display_linklist, ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = []
        current = head
        while current != None:
            node_list.append(current)
            current = current.next

        # only one node to remove
        if len(node_list) == 1:
            return None

        # remove head
        if n == len(node_list):
            return head.next

        # remove tail
        if n == 1:
            node_list[-2].next = None
            return head

        # remove from middle
        pre = node_list[-1 - n]
        post = node_list[1 - n]
        pre.next = post
        return head








# construct LinkList

#val_list = [1, 2, 3, 4, 5]
val_list = [1]
head = create_linklist(val_list)
display_linklist(head)


print("before:")
display_linklist(head)


print("after:")
sol = Solution()
ret = sol.removeNthFromEnd(head, 1)
display_linklist(ret)