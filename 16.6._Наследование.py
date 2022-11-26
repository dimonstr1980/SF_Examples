import datetime


class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False


class Food(Product):
    is_critical = True
    needs_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)


eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)
print(eggs.is_available())


class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event.")


class ItemViewEvent(Event):
    type = "itemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item.")


if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000,
                                    session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)

#     Что получили:
# - Переопределили конструктор класса. Теперь мы используем не родительский, а свой, и передаём в него другой набор аргументов.
# Так у нас получился кастомизированный набор атрибутов: у родительского класса нет атрибута number_of_views.
# - Переопределили значение атрибута type с помощью атрибута класса. Теперь при вызове type от экземпляра нашего дочернего
# класса мы получим значение атрибута type нашего класса ItemViewEvent.
# - Переопределили работу метода show_description: теперь он показывает более специфичное для класса описание.
#
# В некотором смысле, определяя новый класс, вы создаете новый тип данных. Базовые типы данных, предоставляемые Python, так же являются классами.
# Давайте убедимся в этом с помощью функции isinstance. Все просто: вы передаёте в неё объект и тип (класс), а функция возвращает
# логическое значение результата проверки. То есть говорит вам, является ли объект экземпляром указанного класса или нет

print(isinstance("foo", str))
print(isinstance(test_view_event, ItemViewEvent))
print(isinstance(test_view_event, Event))

# Мы видим, что для родительского класса функция также вернёт True.
# На самом деле, по этой и ряду других причин не всегда
# хорошо завязывать логику на проверку типа через isinstance.
#
# Мы уже говорили о том, что в некотором смысле в Python всё — объект.
# Это означает, что под капотом все классы и типы в Python наследуются от object.

print(isinstance("foo", object))

# Классы в Python поддерживают множественное наследование: это значит, что при объявлении класса
# вы можете через запятую в качестве нескольких аргументов перечислить несколько классов.
# При этом порядок перечисления важен, так как от этого будет зависеть, в каком порядке Python будет
# искать одноименные атрибуты и методы, определяя, какой будет кем переопределен.
#
# На практике сложные системы наследования используются не так уж часто. Как правило, берутся
# сторонние готовые библиотеки и модули и выполняется наследование от нужных классов, чтобы дополнить
# и переопределить их логику.
