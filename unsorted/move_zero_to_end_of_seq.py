# Задача: переместить нули в конец 
# Дан массив случайных чисел, необходимо переместить все нули данного массива в конец.
# Например, если задан массив 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0,
# необходимо его изменить к виду: 1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0.
# Порядок остальных элементов должен остаться прежним. Сложность O(n), а пространство О(1)

def moveZero(seq):
    zI = 0
    for i in range(len(seq)):
        if seq[i] != 0:
            seq[i], seq[zI] = seq[zI], seq[i]
            zI += 1

seq = [1, 0, 6, 0, 0, 4, -1, 8]
moveZero(seq)
print(seq)