per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))

for x in per_cent.values():
    i = x * money / 100
    deposit = int(i)
    print(deposit)

deposit_max = int(max(per_cent.values()) * money / 100)
print("Максимальная сумма, которую вы можете заработать — " + str(deposit_max))