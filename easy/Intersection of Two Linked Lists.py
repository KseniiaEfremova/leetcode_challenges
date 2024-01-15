# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    # O(n) time
    # O(1) space
    p1 = headA
    p2 = headB
    while headA is not None and headB is not None:
        if headA.next is None and headB.next is not None:
            headB = headB.next
            p2 = p2.next
        elif headB.next is None and headA.next is not None:
            headA = headA.next
            p1 = p1.next
        else:
            headA = headA.next
            headB = headB.next
    while p1 is not None:
        if p1 == p2:
            return p1.val
        else:
            p1 = p1.next
            p2 = p2.next
    return


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)

node_4 = ListNode(4)
node_5 = ListNode(5)

node_1.next = node_2
node_2.next = node_3
node_4.next = node_5
node_5.next = node_2
