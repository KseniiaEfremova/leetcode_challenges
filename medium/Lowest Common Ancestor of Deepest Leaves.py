from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    d, n = find_deepest_leaves(root)
    return n


def find_deepest_leaves(node):
    if node is None:
        return 0, None
    left_depth, n1 = find_deepest_leaves(node.left)
    right_depth, n2 = find_deepest_leaves(node.right)
    if left_depth == right_depth:
        return left_depth+1, node

    if left_depth > right_depth:
        return left_depth + 1, n1
    return right_depth + 1, n2


node0 = TreeNode(0)
node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2)

node0.left = node1
node0.right = node3
node3.left = node2
