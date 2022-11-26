# Гипотеза Сиракуз заключается в том, что любое натуральное число можно свести к 1,
# если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.

n = int(input('Введите число больше единицы:\n'))
sum = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
        sum += 1
    else:
        n = 3 * n + 1
        sum += 1
print(sum)