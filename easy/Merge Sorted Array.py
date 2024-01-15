def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    free_place = -1
    p1 = m-1
    p2 = n-1
    while free_place >= -len(nums1) and p2 >= 0:
        if p1 < 0 or nums2[p1] > nums1[p2]:
            nums1[free_place] = nums2[p2]
            p2 -= 1
        else:
            nums1[free_place] = nums1[p1]
            p1 -= 1
        free_place -= 1


def foo():
    a = [4, 5, 6, 0, 0, 0]
    b = [1, 2, 3]
    merge(a, 3, b, 3)
    print(a)


foo()