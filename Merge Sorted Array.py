def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    free_place = -1
    p1 = m-1
    p2 = n-1
    while free_place >= -len(nums1) and p2 >= 0:
        if p1 < 0:
            nums1[free_place] = nums2[p2]
            p2 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[free_place] = nums1[p1]
            p1 -= 1
        else:
            nums1[free_place] = nums2[p2]
            p2 -= 1
        free_place -= 1
