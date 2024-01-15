# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if isSameTree(p.left, q.left):
        if isSameTree(p.right, q.right):
            return p.val == q.val
        else:
            return False
    else:
        return False


node1 = TreeNode(1)
node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)

node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

node1a = TreeNode(1)
node2a = TreeNode(2)
# node3a = TreeNode(3)
# node4a = TreeNode(4)
# node5a = TreeNode(5)

node1a.right = node2a
# node1a.right = node3a
# node2a.left = node4a
# node2a.right = node5a

print(isSameTree(node1, node1a))

