def peakIndexInMountainArray(arr: list) -> int:
    i = ((len(arr) + 1) // 2) - 1
    left = 0
    right = len(arr)-1
    while 0 <= i < len(arr):
        if arr[i - 1] < arr[i] < arr[i+1]:
            left = i + 1
            i = i + ((len(arr[left:right]) + 1) // 2)
        elif arr[i - 1] > arr[i] > arr[i+1]:
            right = i
            i = i - ((len(arr[left:right]) + 1) // 2)
        elif arr[i - 1] < arr[i] > arr[i+1]:
            return i


assert peakIndexInMountainArray([1,2,3,4,5,6,5,3,1]) == 5
assert peakIndexInMountainArray([1,2,3,4,5,6,5]) == 5
assert peakIndexInMountainArray([5,6,5,3,1]) == 1
assert peakIndexInMountainArray([5,6,5]) == 1
