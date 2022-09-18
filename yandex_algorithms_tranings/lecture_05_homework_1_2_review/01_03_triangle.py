a = int(input())
b = int(input())
c = int(input())

print('YES' if a + b > c and a + c > b and b + c > a else 'NO')