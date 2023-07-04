class Node:
    def __init__(self, val=0, next_element=None):
        self.next_element = next_element
        self.val = val

    def print_values(self):
        print(self.val, end="")
        node = self.next_element
        while node is not None:
            print(node.val, end="")
            node = node.next_element


l_1 = Node(1)
l_2 = Node(2)
l_4 = Node(4)

r_3 = Node(6)
r_6 = Node(7)
r_8 = Node(8)

l_1.next_element = l_2
l_2.next_element = l_4

r_3.next_element = r_6
r_6.next_element = r_8


def create_linked_list(n):  # n - number of nodes
    if n == 0:
        return None
    linked_list = Node(10)
    linked_list.next_element = create_linked_list(n - 1)
    return linked_list


def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1 is None and list2 is None:
        return None

    if list1.val < list2.val:
        node = list1
        node.next_element = mergeTwoLists(list1.next_element, list2)
    else:
        node = list2
        node.next_element = mergeTwoLists(list1, list2.next_element)
    return node


mergeTwoLists(l_1, r_3).print_values()
