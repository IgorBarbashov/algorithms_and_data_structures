# Дана строка (в кодировке UTF-8)
# Найти самый часто встречающийся в ней символ.
# Если несколько символов встречаются одинаово часто,
# то можно вывести любой.


# Решение #1 - O(N ^ 2)
# Переберем все позиции и для каждой позиции в строке еще раз
# переберем все позиции и в случае совпадения прибавим к счетчику
# единицу. Найдем максимальное значение счетчика

s = input()
ans = ''
anscnt = 0
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print(ans)


# Решение #2 - O(N * K)
# Переберем все символы, встречаюшиеся в строке, а затем переберем
# все позиции и в случае совпадения прибавим к счетчику единицу.
# Найдем максимальное значение счетчика

s = input()
ans = ''
anscnt = 0
for now in set(s):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = now
        anscnt = nowcnt
print(ans)


# Решение #3 - O(N)
# Заведем словарь, где ключом является символ, а значением - сколько
# раз он встретился. Если символ встретился впервые - создаем
# элемент словаря с ключом, совпадающим с этим символом и значеием 0.
# Иначе - прибавляем к элементу словаря с ключом, совпадающим
# с этим символом, единицу.

s = input()
ans = ''
anscnt = 0
dct = {}
for now in s:
    if now not in dct:
        dct[now] = 0
    dct[now] += 1
    if dct[now] > anscnt:
        ans = now
        anscnt = dct[now]
print(ans)
