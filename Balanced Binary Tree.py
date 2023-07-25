# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root) -> bool:
    if root is None:
        return True
    return checkBalance(root.left, root.right)[1]


def checkBalance(left, right):
    if left is None and right is None:
        return 0, True
    d_left, d_right = 0, 0
    if left is not None:
        d_left, res = checkBalance(left.left, left.right)
        d_left += 1
        if not res:
            return 0, False
    if right is not None:
        d_right, res = checkBalance(right.left, right.right)
        d_right += 1
        if not res:
            return 0, False
    count = max(d_left, d_right)
    return count, abs(d_left-d_right) < 2


node_1 = Node()
node_2 = Node()
node_3 = Node()
node_4 = Node()

node_1.left = node_2
node_1.right = node_4
node_2.left = node_3


#
# def isBalanced(root) -> bool:
#     if root is None:
#         return True
#     l = depth(root.left)
#     r = depth(root.right)
#     return abs(l-r) < 2 and isBalanced(root.left) and isBalanced(root.right)
#
#
# def depth(node):
#     if node is None:
#         return 0
#     return max(depth(node.left), depth(node.right)) + 1



