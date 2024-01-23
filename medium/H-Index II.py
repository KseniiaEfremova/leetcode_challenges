def hIndex2(citations):
    n = len(citations)
    left = 0
    right = n

    while left < right:
        middle_indx = (left + right) // 2
        if citations[middle_indx] < n - middle_indx:
            left = middle_indx + 1
        else:
            right = middle_indx

    return n - left


assert hIndex2([0, 0, 4, 4]) == 2
assert hIndex2([0, 1, 1, 2, 2, 3, 3]) == 2
assert hIndex2([0, 1, 1, 2, 3, 3, 3]) == 3
assert hIndex2([0, 1, 1, 1, 1, 1, 3]) == 1
assert hIndex2([0, 1, 1, 2, 3, 3, 6]) == 3
assert hIndex2([0, 1, 1, 4, 4, 4, 4]) == 4
assert hIndex2([0, 1, 2]) == 1
assert hIndex2([0, 1]) == 1
assert hIndex2([0]) == 0
assert hIndex2([1]) == 1
assert hIndex2([100]) == 1
assert hIndex2([0, 0]) == 0
assert hIndex2([3, 3, 3]) == 3
assert hIndex2([4, 5, 5, 5]) == 4
