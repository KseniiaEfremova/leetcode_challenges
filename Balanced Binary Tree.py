# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root) -> bool:
    if root is None:
        return
    return isBalanced(root.left) and isBalanced(root.right)


