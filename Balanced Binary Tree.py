# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkBalance(node):
    if node.left is None and node.right is None:
        return 0, True
    d_left, d_right = 0, 0
    if node.left is not None:
        d_left, balanced = checkBalance(node.left)
        if not balanced:
            return 0, False
        d_left += 1
    if node.right is not None:
        d_right, balanced = checkBalance(node.right)
        if not balanced:
            return 0, False
        d_right += 1
    height = max(d_left, d_right)
    return height, abs(d_left - d_right) < 2


def isBalanced(root) -> bool:
    if root is None:
        return True
    return checkBalance(root)[1]


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



