def getRow(rowIndex: int):
    # O(n**2) time
    # O(n) spice
    res = [1]
    for i in range(rowIndex):
        temp = [0] + res + [0]
        new_row = []
        for k in range(len(temp)-1):
            new_row.append(temp[k]+temp[k+1])
        res = new_row

    return res

print(getRow(4))
