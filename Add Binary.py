def addBinary(a: str, b: str) -> str:
    a = [int(n) for n in list(a)]
    b = [int(n) for n in list(b)]
    sum = []
    rest = 0
    number = 0
    k = -1
    while k > -len(a):
        number = a[k] + b[k]
        if number == 2:
            if rest == 0:
                sum.append(0)
                rest = 1
            else:
                sum.append(1)
                rest = 0
        else:
            sum.append(number)
        if k - 1 == -len(b) - 1:
            if rest == 1:
                sum.append()
                sum.append(a[:k:-1])
        k -= 1



    # if rest == 1:
    #     sum +
