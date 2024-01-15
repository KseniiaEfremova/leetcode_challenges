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
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
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


deleteDuplicates(node_1).print_values()
