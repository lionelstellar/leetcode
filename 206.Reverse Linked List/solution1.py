from construct import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            t = head
            q = head.next
            while q != None:
                r = q.next
                q.next = head
                head = q
                if r != None:
                    q = r
                else:
                    t.next = None
                    return head




