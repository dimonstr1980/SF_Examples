# Лесенка из цифр

n = int(input('Введите число больше единицы:'))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
