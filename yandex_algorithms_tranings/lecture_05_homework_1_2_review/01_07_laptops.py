a, b, c, d = map(int, input().split(' '))
min = (max(a, b) + max(c, d)) * (min(a, b) + min(c, d)) + 1

for i in [a, b]:
    for j in [c, d]:
        n = max(i, j)
        m = a + b - i + c + d - j
        if n * m < min:
            min = n * m
            x = n
            y = m

print(x, y)
