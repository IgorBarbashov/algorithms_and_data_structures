def printAssert(fn, data, expected):
    assert fn(data) == expected, str(data) + ' , expected: ' + str(expected) + ' , actual: ' + str(fn(data))

l = list(map(int, input().split(' ')))

def isListGrow(l):
    if len(l) == 0:
        return 'NO'

    if len(l) == 1:
        return 'YES'

    for i in range(len(l) - 1):
        if l[i + 1] <= l[i]:
            return 'NO'

    return 'YES'

printAssert(isListGrow, [1, 7, 9], 'YES')
printAssert(isListGrow, [1, 9, 7], 'NO')
printAssert(isListGrow, [2, 2, 2], 'NO')

printAssert(isListGrow, [1, 5, 7, 9, 10], 'YES')
printAssert(isListGrow, [], 'NO')
printAssert(isListGrow, [7], 'YES')
printAssert(isListGrow, [1, 7, 9, 2], 'NO')
printAssert(isListGrow, [100, 7, 9, 20], 'NO')

print(isListGrow(l))