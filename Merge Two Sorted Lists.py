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


# def mergeTwoLists(list1, list2):
#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1
#     if list1 is None and list2 is None:
#         return None
#
#     if list1.val < list2.val:
#         node = list1
#         node.next = mergeTwoLists(list1.next, list2)
#     else:
#         node = list2
#         node.next = mergeTwoLists(list1, list2.next)
#     return node


def mergeTwoLists2(list1, list2):
    head = new_list = Node()
    while list1 and list2:
        if list1.val < list2.val:
            new_list.next = list1
            list1 = list1.next
        else:
            new_list.next = list2
            list2 = list2.next
        new_list = new_list.next
    new_list.next = list1 or list2
    return head.next
