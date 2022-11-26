# Декоратор — настолько часто используемая конструкция в Python,
# что ее оформили в качестве «синтаксического сахара».

# Синтаксический сахар в языке программирования — это синтаксические возможности,
# применение которых не влияет на поведение программы, но делает использование
# языка более удобным для человека.

# Пользоваться им можно так:

# @my_decorator
# def my_function():
#     pass

# При этом будет происходить все то же самое, что и:
# my_function = my_decorator(my_function)

# Имейте в виду, что при использовании синтаксического сахара,
# на месте декорируемой функции появляется задекорированная функция!

def my_decorator(fn):
    def wrapper():
        fn()
    return wrapper  # возвращается задекорированная функция, которая заменяет исходную

# выведем незадекорированную функцию
def my_function():
    pass
print(my_function)  # <function my_function at 0x7f938401ba60>

# выведем задекорированную функцию
@my_decorator
def my_function():
    pass
print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>

# Видим, что после декорирования, под названием исходной функции будет не сама функция,
# а функция, которая была внутри декоратора, в данном случае — функция wrapper.

# -----------------------------------------------------------------------------------------

# Передача аргументов в декорируемую функцию.

# До этого мы с вами декорировали только функции без аргументов. Но что будет,
# если мы попытаемся задекорировать функцию с аргументами? wrapper должен уметь принимать
# те же аргументы, что и исходная функция и передавать их в неё. Чтобы не задумываться над
# количеством аргументов и сделать наш декоратор универсальным, мы будем использовать *args и **kwargs.

# Декоратор, в котором встроенная функция умеет принимать аргументы:

def do_it_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_it_twice
def say_word(word):
    print(word)

say_word("Oo!!!")

# Подведем итог по декораторам:

# Декораторы добавляют дополнительное поведение функции без изменения её исходного кода.
# Декораторы — вызовы дополнительных функций, поэтому они немного замедляют ваш код.
# Для передачи аргументов декорируемой функции используйте *args и **kwargs.

# Вот универсальный шаблон для декоратора:

def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper
    
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для
# хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.

def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f"Функция {func} была вызвана {count} раз")
    return wrapper

@counter
def say_word(word):
    print(word)

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз

# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции
# в словаре. Словарь должен находиться в nonlocal области в следующем формате: по ключу
# располагается аргумент функции, по значению результат работы функции, например, {n: f(n)}.

# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы, где будут
# храниться ранее вычисленные значения. Исходная функция, которую нужно задекорировать имеет
# следующий вид и выполняет простое умножение на число 123456789:

def cache(func):
    cache_dict = {}
    def wrapper(num):
        nonlocal cache_dict
        if num not in cache_dict:
            cache_dict[num] = func(num)
            print(f"Добавление результата в кэш: {cache_dict[num]}")
        else:
            print(f"Возвращение результата из кэша: {cache_dict[num]}")
        print(f"Кэш {cache_dict}")
        return cache_dict[num]
    return wrapper

@ cache    
def func(num):
   return num * 123456789

print(func(1))
print(func(2))
print(func(3))
