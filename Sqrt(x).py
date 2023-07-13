def mySqrt(x: int) -> int:
    if x == 1:
        return 1
    high_num = x
    low_num = 0
    while True:
        k = ((high_num - low_num) // 2) + low_num
        if k == low_num or k == high_num:
            return k
        if k**2 == x:
            return k
        if k**2 < x:
            low_num = k
        else:
            high_num = k


assert mySqrt(1) == 1
assert mySqrt(4) == 2
assert mySqrt(8) == 2
assert mySqrt(10) == 3
assert mySqrt(64) == 8
assert mySqrt(15) == 3
assert mySqrt(16) == 4
assert mySqrt(0) == 0

