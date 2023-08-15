# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    res = []
    getOrder(root, res)
    return res


def getOrder(root, l):
    if root is None:
        return
    getOrder(root.left, l)
    getOrder(root.right, l)
    l.append(root.val)
    return l


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3
