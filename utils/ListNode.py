# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def display_linklist(head: ListNode):
    current = head
    ret_str = ""
    while current != None:
        ret_str += str(current.val) + " "
        current = current.next

    print(ret_str.strip())

def create_linklist(val_list: list):
    head = ListNode()
    tail = head
    for _, elem in enumerate(val_list):
        node = ListNode(elem, None)
        tail.next = node
        tail = node
    return head.next

def listnode_test():
    a = [1,2,3,4,5]
    head = create_linklist(a)
    display_linklist(head)

if __name__ == "__main__":
    listnode_test()