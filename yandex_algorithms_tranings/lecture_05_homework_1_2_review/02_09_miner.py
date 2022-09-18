def makeField(h, w, mines):
    dh = [1, 1, 1, 0, 0, -1, -1, -1]
    dw = [1, 0, -1, 1, -1, 1, 0, -1]
    field= []
    for _ in range(h + 2):
        field.append([0] * (w + 2))
    for mh, mw in mines:
        for i in range(len(dh)):
            field[mh + dh[i]][mw + dw[i]] += 1
    for mh, mw in mines:
        field[mh][mw] = '*'
    return field

def printField(n, m, field):
    for h in range(1, n + 1):
        for w in range(1, m + 1):
            print(field[h][w], end = ' ')
        print()

def miner():
    n, m, k = map(int, input().strip().split(' '))
    mines = []
    for _ in range(k):
        mines.append(tuple(map(int, input().strip().split(' '))))
    field = makeField(n, m, mines)
    printField(n, m, field)

miner()