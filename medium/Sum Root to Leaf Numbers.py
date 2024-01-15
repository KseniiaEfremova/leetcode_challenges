from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node4 = TreeNode(4)
node9 = TreeNode(9)
node5 = TreeNode(5)
node1 = TreeNode(1)
node0 = TreeNode(0)
node4.left = node9
node4.right = node0
node9.left = node5
node9.right = node1


def root_to_leaf(root, parent_val):
    if root is None:
        return 0
    total = parent_val*10 + root.val

    if root.left is None and root.right is None:
        return total

    return root_to_leaf(root.left, total) + root_to_leaf(root.right, total)


def sumNumbers(root: Optional[TreeNode]):
    if root is None:
        return 0
    return root_to_leaf(root, 0)


print(sumNumbers(node4))