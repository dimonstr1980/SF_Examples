per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
per_cent_values = list(map(float, per_cent.values()))

for x in per_cent_values:
    deposit = x * money / 100
    print(int(deposit))

deposit_max = int(max(per_cent_values) * money / 100)
print("Максимальная сумма, которую вы можете заработать — " + str(deposit_max))