# Допишите функцию check_h так, чтобы она проверяла гипотезу Сиракуз для числа n.

# Гипотеза Сиракуз заключается в том, что любое натуральное число можно свести к 1,
# если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.

n = int(input('Введите число:\n'))
def check_h(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3 + 1) // 2
        if n == 1:
            return True
    return False