# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
text = input("Enter some text:")
unique_symbols = list(set(text))
print(len(unique_symbols))