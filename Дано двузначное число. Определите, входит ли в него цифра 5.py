# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.

n = int(input("Введите двузначное число: "))

first_digit = n // 10   # проверяем первое число
second_digit = n % 10   # проверяем второе число

print((first_digit == 5) or (second_digit == 5)) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#           Ещё один вариант решения:                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# two_digit = int(input("Введите двузначное число: "))  #
#                                                       #
# if two_digit in range(15, 96, 5):                     #
#     print("Ваше число содержит число 5")              #
# else:                                                 #
#     print("Ваше число не содержит число 5")           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #