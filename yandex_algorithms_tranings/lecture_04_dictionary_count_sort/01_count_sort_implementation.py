def countsort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval + 1)
    count = [0] * k
    for now in seq:
        count[now - minval] += 1
    nowpos = 0
    for val in range(k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
    return seq

seq = [5, 5, 7, 2, 3, 5, 0, 3, 2, 5]
print(countsort(seq))