def climb(n: int, d) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in d:
        return d[n]
    else:
        d[n] = climb(n-1, d) + climb(n-2, d)
    return d[n]


def climbStairs(n):
    d = {}
    a = climb(n, d)
    return a


assert climbStairs(6) == 13
assert climbStairs(3) == 3
assert climbStairs(1) == 1
assert climbStairs(2) == 2
