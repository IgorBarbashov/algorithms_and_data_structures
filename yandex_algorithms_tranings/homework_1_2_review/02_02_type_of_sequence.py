# def printAssert(fn, data, expected):
#     assert fn(data) == expected, str(data) + ' , expected: ' + str(expected) + ' , actual: ' + str(fn(data))

def getTypeOfSequence():
    wasEqual = False
    wasGreater = False
    wasLower = False
    isFirstNumber = True
    prevNumber = 0

    while True:
        n = int(input())

        if n == -2000000000:
            break

        if isFirstNumber:
            isFirstNumber = False
            prevNumber = n
            continue

        if n == prevNumber:
            wasEqual = True
        elif n > prevNumber:
            wasGreater = True
        elif n < prevNumber:
            wasLower = True
        
        prevNumber = n
    
    if isFirstNumber:
        return 'RANDOM'
    if wasGreater and wasLower:
        return 'RANDOM'
    elif (not wasGreater) and (not wasLower):
        return 'CONSTANT'
    elif wasGreater:
        return 'WEAKLY ASCENDING' if wasEqual else 'ASCENDING'
    elif wasLower:
        return 'WEAKLY DESCENDING' if wasEqual else 'DESCENDING'


print(getTypeOfSequence())

# printAssert(getTypeOfSequence, [-530, -530, -530, -530, -530, -530, -2000000000], 'CONSTANT')

# printAssert(getTypeOfSequence, [-2000000000], 'RANDOM')
# printAssert(getTypeOfSequence, [1, -2000000000], 'CONSTANT')

# printAssert(getTypeOfSequence, [1, 2, -2000000000], 'ASCENDING')
# printAssert(getTypeOfSequence, [2, 1, -2000000000], 'DESCENDING')
# printAssert(getTypeOfSequence, [1, 1, -2000000000], 'CONSTANT')

# printAssert(getTypeOfSequence, [1, 2, 3, -2000000000], 'ASCENDING')
# printAssert(getTypeOfSequence, [1, 2, 2, -2000000000], 'WEAKLY ASCENDING')
# printAssert(getTypeOfSequence, [1, 1, 2, -2000000000], 'WEAKLY ASCENDING')

# printAssert(getTypeOfSequence, [3, 2, 1, -2000000000], 'DESCENDING')
# printAssert(getTypeOfSequence, [3, 3, 1, -2000000000], 'WEAKLY DESCENDING')
# printAssert(getTypeOfSequence, [3, 2, 2, -2000000000], 'WEAKLY DESCENDING')

# printAssert(getTypeOfSequence, [1, 3, 2, -2000000000], 'RANDOM')