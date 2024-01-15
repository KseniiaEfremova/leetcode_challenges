def hIndex(citations):
    if len(citations) < 1:
        return 0
    if len(citations) == 1:
        return 0 if citations[0] == 0 else 1
    k = 1
    for i in range(len(citations)-1, -1, -1):
        if citations[i] < k:
            return k-1
        k += 1
    return len(citations)
