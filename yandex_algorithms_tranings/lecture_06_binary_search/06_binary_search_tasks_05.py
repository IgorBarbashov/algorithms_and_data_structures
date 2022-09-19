# Задача #5
# Задана отсортированная по неубыванию последовательность
# из N чисел и число X
# Необходимо определить сколько раз число X входит
# в последовательность

# Решение
def countX(seq, x):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r + 1) // 2
        if seq[m] < x:
            l = m
        else:
            r = m -1
    lli = l if seq[l] < x else -1

    l = 0
    r = len(seq) - 1
    while l < r:
        m = (l + r) // 2
        if seq[m] > x:
            r = m
        else:
            l = m + 1
    fgi = l if seq[l] > x else len(seq)
        
    return fgi - lli - 1

seq = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
print(countX(seq, 5)) # 5

seq = [5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
print(countX(seq, 5)) # 5

seq = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(countX(seq, 5)) # 5

seq = [5]
print(countX(seq, 5)) # 1

seq = [3]
print(countX(seq, 5)) # 0

seq = [10]
print(countX(seq, 5)) # 0

seq = [1, 2, 3, 4]
print(countX(seq, 5)) # 0

seq = [6, 7, 8, 9, 10]
print(countX(seq, 5)) # 0