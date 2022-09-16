# Задача #1
# Дано два числа X и Y без ведущих нулей
# Необходимо проверить, можно ли получить первое
# из второго перестановкой цифр

# Решение
# Посчитаем количество вхождений каждой цифры в каждое
# из чисел и сравним. Цифры будем постепенно добывать
# из числа справа с помощью операций % 10 и // 10

def replace(x, y):
    def countdifits(num):
        dct = [0] * 10
        while num > 0:
            dct[num % 10] += 1
            num //= 10
        return dct

    digx = countdifits(x)
    digy = countdifits(y)

    for d in range(10):
        if digx[d] != digy[d]:
            return False
    return True

print(replace(201, 1201))