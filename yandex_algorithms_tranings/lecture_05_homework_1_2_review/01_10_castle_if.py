a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

minW = min(d, e)
maxW = max(d, e)
minB = min(a, b, c)
midB = a + b + c - minB - max(a, b, c)

print('YES' if minB <= minW and midB <= maxW else 'NO')