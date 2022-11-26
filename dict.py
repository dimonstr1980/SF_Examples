person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['address'] = 'Москва, ул. Кошкина, д. 8, кв. 21'
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person.keys()) # Можно отдельно получить список ключей
print(person.values()) # Или список значений

# Из словаря аналогично спискам можно удалить объект по его ключу.
# Важно помнить, что словарь является неупорядоченным,
# поэтому в функцию pop() всегда нужно передавать ключ удаляемого объекта:
person.pop('phone')

print(person)