# Проверка принадлежности точки к координатной плоскости.

x = int(input("Введите абсциссу:"))
y = int(input("Введите ординату:"))

if x > 0 and y > 0:               # x > 0, y > 0
    print("Первая четверть")
if x > 0 and y < 0:               # x > 0, y < 0
    print("Четвертая четверть")
if x < 0 and y > 0:               # x < 0, y > 0
    print("Вторая четверть")
if x < 0 and y < 0:               # x < 0, y < 0
    print("Третья четверть")