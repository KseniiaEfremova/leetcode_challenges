# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head) -> bool:
    # O(n) time
    # O(1) space
    if head is None or head.next is None:
        return False
    left = head
    right = head.next
    while right is not None:
        if left == right:
            return True
        left = left.next
        if right.next is None:
            return False
        right = right.next.next
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
