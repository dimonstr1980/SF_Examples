"""
Задача. Найти сумму элементов списка
Task. Find sum for elements of the list
"""
list_ = [0, 5, 10, 15, 20]
index = 0
size = 5
sum_ = 0
while index < size:
    sum_ += list_[index]
    index += 1
average = sum_ / size
print(int(average))
"""
Задача. Найти максимальный элемент списка
Task. Find maximum element of the list
---------------------------------------------
Задача. Найти 2-й максимальный элемент списка
Task. Find second maximum element of the list
"""
numbers = [1, 8, 3, 2, 6]
size = 5
current_index = 0
max_number_index = 0
max = numbers[0]
while current_index < size:
    if numbers[current_index] > max:
        max = numbers[current_index]
        max_number_index = current_index
    current_index += 1
print(max)
current_index = 0
second_max = numbers[0]
if max_number_index == 0:
    second_max = numbers[1]
while current_index < size:
    if current_index != max_number_index:
        if numbers[current_index] > second_max:
            second_max = numbers[current_index]
    current_index += 1
print(second_max)
