# Задача #2
# На шахматной доске N x N находятся M ладей (ладья бьет
# клетки на той же горизонтали и вертикали до ближайшей
# занятой)
# Определите, сколько пар ладей бьют друг друга.
# Ладьи задаются парой чисел I и J, обозначающих координаты
# клетки
# 1 <= N <= 10^9, 0 <= M <= 2 * 10^5

# Решение
# Для каждой занятой горизонтали и вертикали будем хранить
# количество ладей на них. Количество пар в горизонтали
# (вертикали) равно количеству ладей минус 1. Суммируем
# это количество пар для всех горизонталей и вертикалей

from re import S


def rookpairs(rooks):
    def addrook(dct, key):
        if key not in dct:
            dct[key] = 0
        dct[key] += 1

    def countpairs(dct):
        pairs = 0
        for key in dct:
            pairs += dct[key] - 1
        return pairs

    dcti = {}
    dctj = {}
    for i, j in rooks:
        addrook(dcti, i)
        addrook(dctj, j)

    return countpairs(dcti) + countpairs(dctj)

print(rookpairs(((0,0), (0,1)))) # 1
print(rookpairs(((0,0), (1,1)))) # 0



# Задача #3
# Дана строка S
# Выведите гистограмму как в примере (коды символов
# отсортированы)
# S = Hello, wolrd!
#       X 
#       XX
# XXXXXXXXXX
#  !,Hdelorw

# Решение
# Для каждого символа в словаре подсчитаем сколько раз он стречался.
# Найдем самый частый символ (n - сколько раз он встречается в строке).
# Гистограмму будем выводить используя n-строк.
# В каждой строке по отсортированным ключам смотрим, если число вхождений
# текущего символа в строке больше номера строки, то выводим символ X,
# иначе - пробел.

def gist(s):
    dct = {}
    for c in s:
        if c not in dct:
            dct[c] = 0
        dct[c] += 1

    maxcount = max(dct.values())
    sorteduniqsyms = sorted(dct.keys())

    for row in range(maxcount, 0, -1):
        for i in sorteduniqsyms:
            if dct[i] >= row:
                print('#', end = '')
            else:
                print(' ', end = '')
        print()
    print(''.join(sorteduniqsyms))

gist('Hello, wolrd!')