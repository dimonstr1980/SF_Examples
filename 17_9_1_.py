L = list(map(int, input("Введите целые числа через пробел:\n").split()))
num = int(input("Введите любое целое число:\n"))
L.append(num)


def binary_search(L, num, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if L[middle] == num:
        return middle
    elif num < L[middle]:
        return binary_search(L, num, left, middle - 1)
    else:
        return binary_search(L, num, middle + 1, right)


for i in range(0, len(L)):
    x = L[i]
    idx = i
    while idx > 0 and L[idx - 1] > x:
        L[idx] = L[idx - 1]
        idx -= 1
    L[idx] = x

print("Сортированный список по возрастанию:", L)
print("Индекс введенного числа:", binary_search(L, num, 0, len(L) - 1))
