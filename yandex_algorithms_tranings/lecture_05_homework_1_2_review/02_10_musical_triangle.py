def musicalTriangle():
    n = int(input().strip())
    notes = []
    for _ in range(n):
        notes.append(tuple(input().strip().split(' ')))
    
    l = 30
    r = 4000
    p = float(notes[0][0])
    for fs, d in notes[1:]:
        f = float(fs)

        if abs(p - f) < 10**(-6):
            continue

        if f > p:
            if d == 'closer':
                l = max(l, (f + p) / 2)
            elif d == 'further':
                r = min(r, (f + p) / 2)
        else:
            if d == 'closer':
                r = min(r, (f + p) / 2)
            elif d == 'further':
                l = max(l, (f + p) / 2)
        p = f

    return (l, r)

print(*musicalTriangle())
