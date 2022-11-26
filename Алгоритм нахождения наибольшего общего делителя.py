# Алгоритм нахождения наибольшего общего делителя.

def e_alg(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a < b:
            b %= a
        else:
            a %= b
    return a + b


print(e_alg(15, 30))
