class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root):
    if root is None:
        return 0
    total = 0
    if root.left is not None and root.left.left is None and root.left.right is None:
        total += root.left.val
    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    return total


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4

# print(sumOfLeftLeaves(node_1))
