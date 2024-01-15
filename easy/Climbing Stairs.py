def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    p1 = 1
    p2 = 2
    for i in range(n - 2):
        f = p1 + p2
        p1 = p2
        p2 = f
    return p2


assert climbStairs(6) == 13
assert climbStairs(3) == 3
assert climbStairs(1) == 1
assert climbStairs(2) == 2
