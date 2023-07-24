# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node5 = Node()
node6 = Node()
node7 = Node()
node1.left = node2
node1.right = node3
node2.left = node7
node3.right = node4
node3.left = node6
node4.left = node5


def minDepth(root) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    md = 10000000
    if root.left is not None:
        md = min(md, minDepth(root.left))
    if root.right is not None:
        md = min(md, minDepth(root.right))
    return md + 1
