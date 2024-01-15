def singleNumber(nums: list) -> int:
    # O(n) time
    # O(1) space
    res = 0
    for n in nums:
        res = n ^ res
    return res


assert singleNumber([1,1,2]) == 2
assert singleNumber([2,1,2]) == 1
assert singleNumber([1,2,2]) == 1