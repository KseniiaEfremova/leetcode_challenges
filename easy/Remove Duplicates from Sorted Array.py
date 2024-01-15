def removeDuplicates(nums) -> int:
    index_place = 0
    pointer = 1
    while pointer < len(nums):
        if nums[pointer] > nums[index_place]:
            nums[index_place + 1] = nums[pointer]
            index_place += 1
        pointer += 1
    return index_place + 1


assert removeDuplicates([1]) == 1
assert removeDuplicates([1, 1, 2]) == 2
assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert removeDuplicates([1, 1]) == 1
