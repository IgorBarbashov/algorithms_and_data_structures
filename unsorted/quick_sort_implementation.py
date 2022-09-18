def partition(seq, start, end):
    p = seq[end]
    pI = start
    for i in range(start, end):
        if seq[i] <= p:
            seq[i], seq[pI] = seq[pI], seq[i]
            pI += 1
    seq[pI], seq[end] = seq[end], seq[pI]
    return pI

def quickSort(seq, start, end):
    if start < end:
        p = partition(seq, start, end)
        quickSort(seq, start, p - 1)
        quickSort(seq, p + 1, end)

seq = [-433, 69, -931, -31, -171, -282, -505, -459, -462, 738, -871, -807, -722, -896, 630, -366, -881, -727, 253, -484, 714, -994, -150, 827, -829, -850, -349, 177, 325, 344, -336, -834, -516, -883, 38, -424, 237, 345, -769, -408, 448, -459, -666, -227, 990, 944, 379, 0, -655, -130, -6, -894, 647, 311, -764, -579, -735, -777, -50, 939, 523, -496, -504, 332, 649, 104, -811, 532, -458, 247, -699, -911, -539, -758, -47, 38, -783, -169, -241]
quickSort(seq, 0, len(seq) - 1)
print(seq)