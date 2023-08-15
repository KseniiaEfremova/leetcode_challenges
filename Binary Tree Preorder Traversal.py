# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root) -> list:
    res = []
    return getOrder(root, res)


def getOrder(root, l: list):
    if root is None:
        return
    l.append(root.val)
    getOrder(root.left, l)
    getOrder(root.right, l)
    return l


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)

node_1.right = node_2
node_2.left = node_3

print(preorderTraversal(node_1))
# for el in preorderTraversal(node_1):
#     print(el)
