def generate(numRows: int):
    # O(n**2) time
    # O(n) spice
    res = [[1]]
    for i in range(numRows-1):
        temp = [0] + res[-1] + [0]
        new_row = []
        for k in range(len(temp)-1):
            new_row.append(temp[k]+temp[k+1])
        res.append(new_row)

    return res

print(generate(6))
