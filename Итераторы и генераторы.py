# ИТЕРАТОРЫ

mylist = [1, 2, 3]
for i in mylist:
    i *= i
    print(i)
    
print('-----------')
    
mylist = [x*x for x in range(1, 4)]
for i in mylist:
    print(i)
    
print('-----------------------')

# ГЕНЕРАТОРЫ
mygenerator = (x*x for x in range(3))
for i in mygenerator :
    print(i)

print('-----------')

def createGenerator() :
    mylist = range(3)
    for i in mylist :
        yield i*i
        
# yield - это ключевое слово, которое используется примерно
# как return — отличие в том, что функция вернёт генератор.

mygenerator = createGenerator() # создаём генератор
print(mygenerator) # mygenerator является объектом!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)
    
print('-----------------------')

# Создаём метод узла, который будет возвращать генератор
def _get_child_candidates(self, distance, min_dist, max_dist):

  # Этот код будет вызываться при каждом обращении к объекту-генератору:

  # Если у узла есть потомок слева
  # И с расстоянием всё в порядке, возвращаем этого потомка
  if self._leftchild and distance - max_dist < self._median:
                yield self._leftchild

  # Если у узла есть потомок справа
  # И с расстоянием всё в порядке, возвращаем этого потомка
  if self._rightchild and distance + max_dist >= self._median:
                yield self._rightchild

  # Если исполнение дошло до этого места, генератор считается пустым

# Создаём пустой список и список со ссылкой на текущий объект
result, candidates = list(), [self]

# Входим в цикл по кандидатам (в начале там только один элемент)
while candidates:

    # Вытягиваем последнего кандидата и удаляем его из списка
    node = candidates.pop()

    # Вычисляем расстояние между объектом и кандидатом
    distance = node._get_dist(obj)

    # Если с расстоянием всё в порядке, добавляем в результат
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    # Добавляем потомков кандидата в список кандидатов,
    # чтобы цикл продолжал исполняться до тех пор,
    # пока не обойдёт всех потомков потомков <...> кандидата
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

return result

# Создаём пустой список и список со ссылкой на текущий объект
result, candidates = list(), [self]

# Входим в цикл по кандидатам (в начале там только один элемент)
while candidates:

    # Вытягиваем последнего кандидата и удаляем его из списка
    node = candidates.pop()

    # Вычисляем расстояние между объектом и кандидатом
    distance = node._get_dist(obj)

    # Если с расстоянием всё в порядке, добавляем в результат
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)

    # Добавляем потомков кандидата в список кандидатов,
    # чтобы цикл продолжал исполняться до тех пор,
    # пока не обойдёт всех потомков потомков <...> кандидата
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

return result

class Bank(): # создаём банк, строящий торговые автоматы (ATM — Automatic Teller Machine)
    crisis = False
    def create_atm(self) :
        while not self.crisis :
            yield "$100"
hsbc = Bank() # когда всё хорошо, можно получить сколько угодно денег с торгового автомата
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.next())

print(corner_street_atm.next())

print([corner_street_atm.next() for cash in range(5)])

hsbc.crisis = True # пришёл кризис, денег больше нет!
print(corner_street_atm.next())

wall_street_atm = hsbc.create_atm() # что верно даже для новых автоматов
print(wall_street_atm.next())

hsbc.crisis = False # проблема в том, что когда кризис прошёл, автоматы по-прежнему пустые...
print(corner_street_atm.next())

brand_new_atm = hsbc.create_atm() # но если построить ещё один, будешь снова в деле!
for cash in brand_new_atm :
    print cash
    
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)

print(list(itertools.permutations(horses)))