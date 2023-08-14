# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list):
    lenn = len(nums)
    i = ((lenn + 1) // 2) - 1
    return biuldBST(lenn, i, nums)


def biuldBST(lenn, i, nums):
    if lenn == 1:
        return Node(nums[i])
    if lenn == 0:
        return None
    root = Node(nums[i])
    root.left = biuldBST(i, i - (((lenn + 1) // 2) - 1), nums)
    root.right = biuldBST(i, i + (((lenn + 1) // 2) - 1), nums)
    return root


arr = [1,2,3]








#     if len(nums) == 1:
#         return Node(nums[0])
#     if len(nums) == 0:
#         return None
#     mid = (len(nums)+1) // 2
#     root = Node(nums[mid-1])
#     root.left = sortedArrayToBST(nums[:mid-1])
#     root.right = sortedArrayToBST(nums[mid:])
#     return root
#
#
# def biuldBST(root, arr):

