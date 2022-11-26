# Словари в Python

# Чтобы работать со словарём, его нужно создать.
# Сделать это можно несколькими способами. Во-первых, с помощью литерала:
d = {}
print(d)

d = {'dict': 1, 'dictionary': 2}
print(d)

# Во-вторых, с помощью функции dict:

d = dict(short='dict', long='dictionary')
print(d)

d = dict([(1, 1), (2, 4)])
print(d)

# В-третьих, с помощью метода fromkeys:

d = dict.fromkeys(['a', 'b'])
print(d)

d = dict.fromkeys(['a', 'b'], 100)
print(d)

# В-четвертых, с помощью генераторов словарей:

d = {a: a ** 2 for a in range(7)}
print(d)