class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_values(self):
        print(self.val, end="")
        node = self.next
        while node is not None:
            print(node.val, end="")
            node = node.next


def deleteDuplicates(head):
    if head is None:
        return None
    if head.next is None:
        return head
    head.next = deleteDuplicates(head.next)
    if head.val == head.next.val:
        return head.next
    else:
        return head


node_1 = ListNode(1)
node_2 = ListNode(1)
node_3 = ListNode(2)
node_4 = ListNode(3)
node_5 = ListNode(3)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

deleteDuplicates(node_5).print_values()
