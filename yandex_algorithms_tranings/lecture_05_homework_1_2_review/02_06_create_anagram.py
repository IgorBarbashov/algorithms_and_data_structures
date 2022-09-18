# def printAssert(fn, data, expected):
#     assert fn(data) == expected, str(data) + ' , expected: ' + str(expected) + ' , actual: ' + str(fn(data))

def isAnagram(seq):
    for i in range(len(seq) // 2):
        if seq[i] != seq[len(seq) - 1 - i]:
            return False
    return True

def concatSeq(seq, addSeq):
    resSeq = []
    for s in seq:
        resSeq.append(s)
    for s in addSeq:
        resSeq.append(s)
    return resSeq

def createAnagram(seq, n):
    addSeq = []

    for i in range(n):
        if isAnagram(concatSeq(seq, addSeq)):
            print(len(addSeq))
            print(*addSeq)
            return

        addSeq.insert(0, seq[i])


n = int(input())
seq = list(map(int, input().strip().split(' ')))
createAnagram(seq, n)

# upd - надо было сделать strip() перед разбиением входной строки на числа
# проверяющая система выдает RE на 8 тесте
# решение алгоритмически такое же как в разобрах ДЗ (есть разница в имплементации)
# локально все считается (возможно проблема в версиях компилятора python)
# данные теста:
# 91
# 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 3 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 
