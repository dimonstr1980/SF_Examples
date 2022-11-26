# Лесенка с помощью цикла while

y = int(input("Введите число ступенек: "))
y = y * 2
out = ' '
x = 1
while x < y + 1:
    if x % 2 == 0:
        print(out, "|")
    else:
        print(out, "_")
    out += ' '
    x += 1