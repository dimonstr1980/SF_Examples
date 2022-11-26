letters = ['a', 'b', 'c', 'd', 'e'] # создание списка
letters.append('f') # добавить элемент последним в список
letters.append('g') # и тут
letters.sort() # сортирует список
letters.reverse() # сортирует список в обратном порядке
letters.pop(0) # удалить элемент из списка по индексу (без индекса - последний)
letters.remove('c') # удаляет первое вхождение значения в списке
letters.extend(['h', 'i']) # расширяет список, добавляя элементы. Преимущество над append в том, что вы можете добавлять списки
letters.insert(-1, 'z') # вставляет элемент перед указанным индексом
print('элементы нашего списка: ' + str(letters))
print('длина нашего списка: ' + str(len(letters)))
print('последний элемент в нём: ' + letters[-1])
print(letters[::2]) # вывод элементов с первого по последний с шагом 2 (через один)
print(letters.index('b')) # вывод индекса известного элемента
print(letters.count('c')) # считаем кол-во известных (запрашиваемых) элементов
print(', '.join(letters)) # преобразование списка в строку
print('\n'.join(letters)) # построчный вывод списка



per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
per_cent_values = list(map(float, per_cent.values()))

for x in per_cent_values:
    deposit = x * money / 100
    print(int(deposit))

deposit_max = int(max(per_cent_values) * money / 100)
print("Максимальная сумма, которую вы можете заработать — " + str(deposit_max))