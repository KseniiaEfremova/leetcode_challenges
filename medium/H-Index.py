def hIndex(citations):
    if len(citations) < 1:
        return 0
    if len(citations) == 1:
        return 0 if citations[0] == 0 else 1
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)



assert hIndex([3,0,6,1,5]) == 3
assert hIndex([1,3,1]) == 1
assert hIndex([10,8,5,4,3]) == 4
assert hIndex([10,8,5,3,3]) == 3
assert hIndex([10]) == 1
assert hIndex([0]) == 0
assert hIndex([]) == 0
assert hIndex([11,10]) == 2
assert hIndex([]) == 0

q = [3,0,6,1,5]
print(hIndex(q))