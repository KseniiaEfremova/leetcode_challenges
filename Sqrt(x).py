def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x < 4:
        return 1
    power = 0
    k = 2
    d = {}
    while k**2 <= x:
        while k**power <= x:
            if k**power <= x <= k**(power+1):
                d[k] = x-k**power
            power += 1
        k += 1
        power = 0
    closest_num = min(d.values())
    res = 0
    for key in d:
        if closest_num <= d[key]:
            res = key
    return res


assert mySqrt(1) == 1
assert mySqrt(4) == 2
assert mySqrt(8) == 2
assert mySqrt(10) == 3
assert mySqrt(64) == 8
assert mySqrt(15) == 3
assert mySqrt(4) == 2
