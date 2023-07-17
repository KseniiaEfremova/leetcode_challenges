def mySqrt(x: int) -> int:
    high_num = x
    low_num = 0
    while low_num != high_num:
        k = ((high_num - low_num + 1) // 2) + low_num
        k2 = k ** 2
        if k2 == x:
            return k
        if k2 < x:
            low_num = k
        else:
            high_num = k - 1
    return low_num


assert mySqrt(1) == 1
assert mySqrt(4) == 2
assert mySqrt(8) == 2
assert mySqrt(10) == 3
assert mySqrt(64) == 8
assert mySqrt(15) == 3
assert mySqrt(16) == 4
assert mySqrt(0) == 0

