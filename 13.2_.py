print(str(123456789))
# 123456789
print(list(str(123456789)))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_digit = list(map(int, list(str(123456789))))
print(5 in list_digit)
# True
# Но на самом деле эту задачу можно было решить намного проще:
print('5' in str(123456789))
# True
N = 1234567890
print('3' in str(N) and '7' in str(N))
# True