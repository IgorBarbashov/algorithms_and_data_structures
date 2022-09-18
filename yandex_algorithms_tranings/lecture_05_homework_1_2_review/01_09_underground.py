a = int(input())
b = int(input())
n = int(input())
m = int(input())

minA = n + (n - 1) * a
maxA = minA + 2 * a

minB = m + (m - 1) * b
maxB = minB + 2 * b

if minA > maxB or minB > maxA:
    print(-1)
    exit()

print(max(minA, minB), min(maxA, maxB))