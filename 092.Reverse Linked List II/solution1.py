from construct import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head2 = head
        while head2.val != left:
            tail1 = head2
            head2 = head2.next


        while


