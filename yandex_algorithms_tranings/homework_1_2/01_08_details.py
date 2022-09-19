n, k, m = map(int, input().split(' '))
ostatok = n
det = 0

if k <= n and m <= k:
    while ostatok >= k:
        zag = ostatok // k
        det += (k // m) * zag
        ostatok = ostatok % k + (k % m) * zag

print(det)