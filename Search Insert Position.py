import bisect


def searchInsert(nums: list, target: int) -> int:
    return bisect.bisect_left(nums, target)


assert searchInsert([1,3,5,6], 5) == 2
assert searchInsert([1,3,5,6], 2) == 1
assert searchInsert([1,3,5,6], 7) == 4
assert searchInsert([1,3,5,6], 0) == 0
