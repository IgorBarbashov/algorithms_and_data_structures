## Как устроено множество
- Что должно уметь делать множество
  - добавлять элемент
  - проверять наличие элемента
  - удалять элемент
- Пример организации мульти-множества на списках (множество значений хэш-функции = N, кол-во элементов = K)
  - добавление элемента - O(1)
  - поиск элемента - производится линейным поиском - O (N + K) (в среднем это O(K/N))
  - удаление элемента - O(1) (но перед этим надо выполнить поиск в среднем за O(K/N))

```
Мульти-множество - это множество, в которое один и тот же элемент может входить много раз
```

```
Хэш-таблица - структура у которой ключ - это значение хэш-функции, а значение - список элементов для которых значение хэш-функции = ключу (для которых произошла коллизия при вычислении хэш-функции)
```

```
Коллизия - совпадение значений хэш-функции для разных апарметров
```

## Что можно хранить в множестве эффективно
- В общем случае хранить можно что угодно
- **Эффективно** - только неизменяемые объекты
- Для неизменяемых объектов можно посчитать значение хэш-функции при их создании
- Хэш-функция должна давать равномерное распределение


## Амортизированная сложность
- Проблемы с хэш-таблицей
  - слишком большой размер - ест много памяти O(N)
  - слишком маленький размер - большой коэффициент заполнения и медленный поиск и удаление O(K/N)
  - хочется иметь разумный баланс, например, коэффициент заполнения не больше единицы (т.е. K <= N). Тогда все операции в среднем будут занимать O(1)
- Решение проблемы с хэш-таблицей
  - когда таблица наполнится - увеличим ее размер вдвое и перестроим
  - **сложность добавления N элементов O(N)**

```
Амортизированная сложность - среднее время выполнения операции (условно)
```

- у нас амортизированная сложность операции O(1) - всего было N операций и суммарно на это ушло O(N)
- в худшем случае отдельная операция выполняется за O(N) - может не подходить для систем реального времени