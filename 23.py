# Definition for singly-linked list.
#最小堆
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    def mergeKLists(self, lists):
        
        #:type lists: List[ListNode]
        #:rtype: ListNode

        empty = 1
        k = len(lists)
        i = 0
        while empty and i < k:
            if lists[i] != []:
                empty = 0
            i += 1
        if empty == 1:
            return ListNode(None)

        else:
            tmpNode = lists
            tmpVal = [tmpNode[i].val for i in range(k)]
            head = ListNode(None)
            tail = head
            while len(tmpNode) > 0:
                min_index = self.findmin(tmpNode)
                insert_node = ListNode(tmpNode[min_index].val)
                tail.next = insert_node
                tail = tail.next
                if tmpNode[min_index].next == None:
                    tmpNode.remove(tmpNode[min_index])
                else:
                    tmpNode[min_index] = tmpNode[min_index].next
                ret = showLN(head)
            return head.next

    def findmin(self, list):
        min = list[0].val
        min_index = 0
        for i in range(len(list)):
            if list[i].val < min:
                min = list[i].val
                min_index = i
        return min_index


def createLN(list):
    h = ListNode(None)
    t = h
    for elem in list:
        tmp = ListNode(elem)
        t.next = tmp
        t = t.next
    return h.next

def showLN(ListNode):
    t = ListNode
    list = []
    while t != None:
        list.append(t.val)
        t = t.next
    #print(list)
    return list

input = [createLN([1,2,3]), createLN([1,2,3])]
input = [[]]

s = Solution()
print(s.mergeKLists(input))
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        if lists == []:
            return None
        else:
            k = len(lists)
            if k == 1:
                return lists[0]
            elif k == 2:
                return self.merge2(lists[0], lists[1])
            else:
                left =  []
                right = []

                for i in range(k // 2):
                    left.append(lists[i])
                for i in range(k // 2, k):
                    right.append(lists[i])

                return self.merge2(self.mergeKLists(left), self.mergeKLists(right))

    def merge2(self, l1, l2):
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

def showLN(ListNode):
    t = ListNode
    list = []
    while t != None:
        list.append(t.val)
        t = t.next
    #print(list)
    return list

l1 = ListNode(1)
l2 = ListNode(2)
l3 = None
L=[l1,l2,l3]
s=Solution()
showLN(s.mergeKLists(L))