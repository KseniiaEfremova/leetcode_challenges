# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root) -> bool:
    return root is None or isMirror(root.left, root.right)


def isMirror(left, right) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(4)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(2)
node7 = TreeNode(4)

node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3
node6.left = node5
node6.right = node7

