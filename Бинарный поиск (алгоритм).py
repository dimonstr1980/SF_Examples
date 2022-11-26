# Бинарный поиск (алгоритм)

def bi_search(a: int, array: list) -> int:
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left


print(bi_search(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
