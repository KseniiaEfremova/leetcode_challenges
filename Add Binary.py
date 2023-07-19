def addBinary(a: str, b: str) -> str:
    res = []
    n = max(len(a), len(b))
    carry = 0
    for i in range(n):
        ia = len(a) - 1 - i
        ib = len(b) - 1 - i
        ca = int(a[ia]) if ia >= 0 else 0
        cb = int(b[ib]) if ib >= 0 else 0
        t = carry + ca + cb
        res.append(t % 2)
        carry = t // 2
    if carry > 0:
        res.append(carry)
    return ''.join(str(res[i]) for i in range(len(res) - 1, -1, -1))
