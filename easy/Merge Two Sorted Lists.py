class Node:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def print_values(self):
        print(self.val, end="-")
        node = self.next
        while node is not None:
            print(node.val, end="-")
            node = node.next


l_1 = Node(1)
l_3 = Node(3)
l_5 = Node(5)
l_9 = Node(9)

r_2 = Node(2)
r_10 = Node(10)

l_1.next = l_3
l_3.next = l_5
l_5.next = l_9

r_2.next = r_10


def mergeTwoLists(list1, list2):
    head = curr = Node()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    return head.next