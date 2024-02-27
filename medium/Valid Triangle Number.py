from typing import List


def triangleNumber(nums: List[int]) -> int:
    total = 0
    for i in range(len(nums)-2):
        first_side = nums[i]
        for j in range(i+1, len(nums)-1):
            second_side = nums[j]
            for k in range(j+1, len(nums)):
                third_side = nums[k]
                if (first_side + second_side > third_side and
                        first_side + third_side > second_side and second_side + third_side > first_side):
                    total += 1
    return total


q = [24,3,82,22,35,84,19]
print(triangleNumber(q))

assert triangleNumber([4,2,3,4]) == 4
assert triangleNumber([7,0,0,0]) == 0
assert triangleNumber([2,2,3,4]) == 3
assert triangleNumber([24,3,82,22,35,84,19]) == 10
assert triangleNumber([4,2,3,4]) == 4
assert triangleNumber([4,2,3,4]) == 4



