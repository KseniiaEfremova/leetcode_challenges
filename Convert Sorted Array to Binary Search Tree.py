# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list):
    if len(nums) == 1:
        return Node(nums[0])
    if len(nums) == 0:
        return None
    mid = (len(nums)+1) // 2
    root = Node(nums[mid-1])
    root.left = sortedArrayToBST(nums[:mid-1])
    root.right = sortedArrayToBST(nums[mid:])
    return root
