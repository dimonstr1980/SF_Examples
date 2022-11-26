# Последовательность Фибоначчи. Определение заданного числа в последовательности

def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)
        
print(rec_fibb(12))

def fib():
    a, b = 0, 1
    yield a
    yield b
    
    while True:
        a, b = b, a + b
        yield b
   
for i in fib():
    print(i)