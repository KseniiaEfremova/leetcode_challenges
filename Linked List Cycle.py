# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head) -> bool:
    d = {}
    while head is not None:
        d[head] = 0
        if head.next in d:
            return True
        head = head.next
    return False



node_3 = ListNode(3)
node_2 = ListNode(2)
node_0 = ListNode(0)
node_4 = ListNode(4)

node_3.next = node_2
node_2.next = node_0
node_0.next = node_4
node_4.next = node_2

print(hasCycle(node_3))
