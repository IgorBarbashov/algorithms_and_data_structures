# def printAssert(fn, data, expected):
#     assert fn(data) == expected, str(data) + ' , expected: ' + str(expected) + ' , actual: ' + str(fn(data))

def abs(x):
    return -x if x < 0 else x

def findNearest(l, x):
    nearest = l[0]
    for i in range(1, len(l)):
        if abs(l[i] - x) < abs(nearest - x):
            nearest = l[i]
    print(nearest)

n = int(input())
l = list(map(int, input().split(' ')))
x = int(input())
findNearest(l, x)