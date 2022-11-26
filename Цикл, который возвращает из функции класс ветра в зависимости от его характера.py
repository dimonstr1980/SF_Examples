# Цикл, который возвращает из функции класс ветра в зависимости от его характера:

def get_wind_class(speed):  # Объявление функции
    if 1 <= speed <= 4:
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"
print(get_wind_class(25))  # Печатаем результат выполнения