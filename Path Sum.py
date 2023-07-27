# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = Node(-2)
node2 = Node(-3)
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
    return checkPathSum(root, targetSum, 0)


def checkPathSum(root, targetSum, curSum):
    if root is None:
        return False
    curSum = curSum + root.val
    # if curSum > targetSum:
    #     return False
    if root.left is None and root.right is None and curSum == targetSum:
        return True
    if root.left is None and root.right is None and curSum != targetSum:
        return False
    return checkPathSum(root.left, targetSum, curSum) or checkPathSum(root.right, targetSum, curSum)


print(hasPathSum(node1, -5))