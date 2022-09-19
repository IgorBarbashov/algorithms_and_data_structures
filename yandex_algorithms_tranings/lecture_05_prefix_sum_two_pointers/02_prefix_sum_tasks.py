# Задача #1
# Дана последовательность чисел длиной N и M запросов
# Запросы: 'Сколько нулей на полуинтервале [L, R)'

# Решение
# Для каждого префикса посчитаем количество нулей на нем
# (prefixZeros). Тогда ответ на запрос на полуинтервале [L, R)
# prefixZeros[r] - prefixZeros[l]

def makePrefix(seq):
    prefixZeros = [0] * (len(seq) + 1)
    for i in range(1, len(prefixZeros)):
        if seq[i - 1] == 0:
            prefixZeros[i] = prefixZeros[i - 1] + 1
        else:
            prefixZeros[i] = prefixZeros[i - 1]
    return prefixZeros

def countZero(prefixZeros, l, r):
    return prefixZeros[r] - prefixZeros[l]

seq = [2, 0, 1, 0, -4]
prefixZeros = makePrefix(seq)
print(countZero(prefixZeros, 0, 5)) # 2



# Задача #2
# Дана последовательность чисел длиной N
# Необходимо найти количество отрезков с нулевой суммой

# Решение
# За O(N) посчитаем префиксные суммы, но хранить их будем не в массиве,
# а в словаре, где key = префиксной сумме, а value = ко-ву раз,
# сколько эта префиксная сумма встречается на всей последовательности
# Тогда кол-во отрезков нулевой длины = сумме (values - 1) по всем
# ключам словаря

def makePrefix(seq):
    dct = {0 : 1}
    nowsum = 0
    for now in seq:
        nowsum += now
        if nowsum not in dct:
            dct[nowsum] = 0
        dct[nowsum] += 1
    return dct

def countZeros(dct):
    count = 0
    for nowsum in dct:
        countsum = dct[nowsum]
        count += countsum * (countsum - 1) // 2
    return count
