S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)

####################################
#         Код по существу          #
####################################
# S = 0                            #
# N = 5                            #
#                                  #
# for i in range(1, N + 1):        #
#     S += i                       #
# print("Ответ: сумма равна = ", S)#
####################################
#     Здесь цикл произведения      #
####################################
# P = 1                            #
# N = 5                            #
#                                  #
# for i in range(1, N + 1):        #
#     P *= i                       #
# print("Ответ: сумма равна = ", P)#
####################################