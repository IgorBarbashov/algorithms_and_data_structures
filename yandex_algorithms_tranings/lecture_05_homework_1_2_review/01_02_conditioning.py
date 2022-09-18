troom, tcond = map(int, input().split(' '))
mode = input()

if mode == 'auto':
    print(tcond)
elif mode == 'fan':
    print(troom)
elif mode == 'freeze':
    print(min(troom, tcond))
elif mode == 'heat':
    print(max(troom, tcond))