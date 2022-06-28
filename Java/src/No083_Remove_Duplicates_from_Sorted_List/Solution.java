package No083_Remove_Duplicates_from_Sorted_List;

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode current = head;
        int now = head.val;
        while (current.next != null) {

            if (now == current.next.val) {
                current.next = current.next.next;
            } else {
                now = current.next.val;
                current = current.next;
            }
        }
        return head;
    }
}