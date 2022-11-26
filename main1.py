# Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:

# 1. Первое и последнее числа последовательности должны поменяться местами.
# 2. В конец списка нужно добавить сумму всех чисел.

string = input("Введите числа через пробел:")
list_of_strings = string.split()
list_of_numbers = list(map(int, list_of_strings))
list_of_numbers.reverse()
list_of_numbers.append(sum(list_of_numbers))
print(list_of_numbers)
