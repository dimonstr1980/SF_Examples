# Алгоритмы сортировки

# 1. Наивная сортировка, или как делать плохо, т.к. долго


import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счётчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счётчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем, отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print('Наивная сортировка', array)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)  # 290698


# 2. Сортировка выбором


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = len(array) / 2 * 10  # количество сравнений, которые производятся в алгоритме

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print('Сортировка выбором', array)
print(int(count))

# тот же алгоритм, но теперь сортируем список по убыванию
for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print('Сортировка выбором, по убыванию', array)


# 3. Сортировка пузырьком (самый любимый способ у студентов)


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print('Сортировка пузырьком', array)


# 4. Сортировка вставками


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0
pere = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    count += 1
    while idx > 0 and array[idx - 1] > x:
        array[idx] = array[idx - 1]
        idx -= 1
        pere += 1
        array[idx] = x

print('Сортировка вставками', array)
print(pere)  # выводим количество перестановок за цикл
print(int(count * (count - 1) / 2))  # выводим количество сравнений


# 5. Сортировка слиянием


def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если длина массива равна 2,
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    while i < len(left) and j < len(right):  # пока указатели не вышли за границы
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):  # добавляем хвосты
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print('Сортировка слиянием', merge_sort(array))

# 6. Быстрая сортировка


def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Не забудьте что-нибудь вернуть!
        return sort(less) + equal + sort(greater)  # используйте оператор + для объединения списков
    # обратите внимание, что вы хотите равный, а не сводный
    else:  # Вам нужно обработать часть в конце рекурсии --
        return array  # когда у вас есть только один элемент в вашем массиве, просто верните его.


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print('Быстрая сортировка', sort(array))


# 6.1 Ещё один вариант быстрой сортировки


def quicksort(alist, start, end):
    """Сортировка списка от 'start' до 'end - 1' включительно."""
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


alist = input('Введите список номеров через пробел: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('И это - быстрая сортировка: ', end='')
print(alist)
