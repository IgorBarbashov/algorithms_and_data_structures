## Сортировка подсчетом
- Пусть необходимо отсортировать массив из N целых чисел, каждое от 0 до K
- Обычная сортировка займет O(N * log(N))
- Будем считать количество вхождений каждого числа, а задем выводить каждое число столько раз, сколько оно встречалось. Это займет O(N + K) и O(K) дополнительной памяти
- Интервал значений можно сдвинуть, чтобы он был не от 0 до K, а от минимального до максимального значения в массиве

## Словари
- Словарь - как **множество**, но к каждому ключу приписано значение
- Искать по значению в словаре **нельзя**!
- Константа в сложности словарей заметно больше, чем у массивов, поэтому где можно - **лучше использовать** сортировку подсчетом
- Сортирову подсчетом неразумно использовать, если **данные разреженные**