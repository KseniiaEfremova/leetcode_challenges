def removeElement(nums, val: int) -> int:
    place = 0
    pointer = 0
    while pointer < len(nums):
        if nums[pointer] != val:
            nums[place] = nums[pointer]
            place += 1
        pointer += 1
    return place


assert removeElement([0,2,0,0,1], 0) == 2
assert removeElement([1,2,0,1,1], 0) == 4
assert removeElement([0,0,0,0,0], 0) == 0
assert removeElement([0,1,2,2,3,0,4,2], 2) == 5
assert removeElement([0,2,0,0,1], 3) == 5


