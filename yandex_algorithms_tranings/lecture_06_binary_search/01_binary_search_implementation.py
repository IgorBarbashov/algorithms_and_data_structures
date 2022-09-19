def leftBinSearch(l, r, checkFn, checkParams):
    while l < r:
        m = (l + r) // 2
        if checkFn(m, checkParams):
            r = m
        else:
            l = m + 1
    return l

def rightBinSearch(l, r, checkFn, checkParams):
    while l < r:
        m = (l + r + 1) // 2
        if checkFn(m, checkParams):
            l = m
        else:
            r = m - 1
    return l
