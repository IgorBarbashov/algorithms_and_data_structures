setsize = 10
myset = [[] for _ in range(setsize)]

def hashFn(x):
    return x % setsize

def add(x):
    myset[hashFn(x)].append(x)

def has(x):
    for el in myset[hashFn(x)]:
        if el == x:
            return True
    return False

def delete(x):
    xlist = myset[hashFn(x)]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
