from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    inorderTraversalRec(root, result)
    return result


def inorderTraversalRec(root: Optional[TreeNode], result: List[int]):
    if root is None:
        return
    inorderTraversalRec(root.left, result)
    result.append(root.val)
    inorderTraversalRec(root.right, result)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node4.left = node2
node4.right = node5
node2.left = node1
node2.right = node3
node5.left = node6
node5.right = node7
