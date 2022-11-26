# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.
book = {}
book['title'] = input("Enter the book's name:")
book['author_last_name'] = input("Enter the author last name:")
book['year_release'] = int(input("Enter the year release of the book:"))
print(book)