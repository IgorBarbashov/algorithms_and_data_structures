# Задача #4
# Сгруппировать слова по общим буквам
# Sample input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# Sample output: [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

# Решение
# Отсортируем в каждом слове буквы и это будет выступать в роли
# ключа, а значением будет список слов

def group(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedwords in groups:
        ans.append(groups[sortedwords])
    return ans

print(group(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# Возможные проблемы решения
# Вдруг слово будет длинное (N)? Сортировка займет O(N * log(N))
# Количество различных букв в слове K <= N, можем посчитать кол-во
# каждой за O(N) и отсортировать за O(K * log(K)), теоретически


# Задел для возможных оптимизаций
# Будет тормозить - посмотрим на профилировщике где, и если долго
# считается ключ - легко поправим на что-то более эффективное
# Для этого выделим сортировку ключа в отдельную функцию

def group(words):
    def sortkey(key):
        return ''.join(sorted(word))

    groups = {}
    for word in words:
        sortedword = sortkey(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedwords in groups:
        ans.append(groups[sortedwords])
    return ans