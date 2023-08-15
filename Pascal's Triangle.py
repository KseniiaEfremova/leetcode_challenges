def generate(numRows: int):
    # O(n**2) time
    # O(n**2) space
    res = [[1]]
    for i in range(numRows - 1):
        new_row = []
        new_row.append(1)
        temp = res[-1]
        for k in range(len(temp) - 1):
            new_row.append(temp[k] + temp[k + 1])
        new_row.append(1)
        res.append(new_row)

    return res

print(generate(4))