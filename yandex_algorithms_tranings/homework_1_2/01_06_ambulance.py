# WA
k1, m, k2, p2, n2 = map(int, input().split(' '))


# противоречивые данные
# - несовпадение кол-ва этажей
#   - n2 > m
if n2 > m:
    print(-1, -1)
    quit()



if (n2 - 1 + (p2 - 1) * m) == 0:
    p1 = 0
    if m == 1:
        print(0, 1)
    else:
        print(0, 0)
    quit()

else:
    if k2 == (p2 - 1) * m:
        print(-1, -1)
        quit()

    x = k2 // (n2 - 1 + (p2 - 1) * m)

    if x < 1:
        print(-1, -1)
        quit()
    
    kp = m * x
    p1 = k1 // kp + (0 if k1 % kp == 0 else 1)

    n1 = (k1 % kp) // x + (0 if (k1 % kp) % x == 0 else 1)
    print(p1, n1)