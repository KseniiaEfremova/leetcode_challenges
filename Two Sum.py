def twoSum(nums, target):
    # O(n) - time
    # O(len(d)) - space
    if len(nums) == 2:
        return [0, 1]
    d = dict()
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]].append(i)
        else:
            d[nums[i]] = [i]
    for key in d:
        if key == (target - key) and len(d[key]) > 1:
            return d[key][0:2]
        if target - key in d and key != (target - key):
            res = d[key] + d[target - key]
            res.sort()
            return res
    return False


assert twoSum([3,2,3], 6) == [0, 2]
assert twoSum([3,3,3], 6) == [0, 1]
assert twoSum([3,2], 5) == [0, 1]
assert twoSum([2,11,15,7], 9) == [0, 3]
assert twoSum([3,2,4], 6) == [1,2]
assert twoSum([3,2,3,1,2,3,4,5,7], 1) == False


def twoSum_(nums, target):
    # O(nlogn) - time
    # O(n) - space
    if len(nums) == 2:
        return [0, 1]
    d = dict()
    nums.sort()
    left = 0
    right = len(nums)-1
    while True:
        if left == right:
            return False
        if nums[left] + nums[right] == target:
            if nums[left] == nums[right]:
                return d[nums[left]][0:2]
            else:
                return d[nums[left]] + d[nums[right]]
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1