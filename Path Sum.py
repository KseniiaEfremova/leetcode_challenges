# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.left = node2
# node1.right = node4
# node2.right = node3
# node4.right = node5


def hasPathSum(root, targetSum: int) -> bool:
    if root is None:
        return False
    if targetSum < 0:
        return False
    if targetSum == 0:
        return True
    else:
        return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


print(hasPathSum(node1, 1))