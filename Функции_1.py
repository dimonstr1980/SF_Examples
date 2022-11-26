# Напишите функцию, которая проверяет, является ли число n делителем числа a.
# И выводит на экран соответствующее сообщение, является ли число делителем или нет.

def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5

# Напишите функцию, которая печатает «обратную лесенку» следующего типа:

def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)

# Напишите функцию, которая будет возвращать количество делителей числа а.
# Пример ввода: 5    Пример вывода программы: 2

def get_multipliers(a):
   count = 0
   for n in range(1, a + 1):
       if a % n == 0:
           count += 1

   return count

get_multipliers(5)  # 2
get_multipliers(4)  # 3

# Напишите функцию, которая проверяет, является ли данная строка
# палиндромом или нет, и возвращает результат проверки. Пример:
#   check_palindrome("test")  # False
#   check_palindrome("Кит на море не романтик")  # True

def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True