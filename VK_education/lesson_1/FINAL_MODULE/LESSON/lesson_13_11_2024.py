import collections
import functools
import time
import itertools
# Demonstrations Collections in Python
l1 = [1, 1, 3, 3, 3, 6, 7, 8, 8]
counter = collections.Counter(l1)
dec = collections.deque(l1)
dec.append(4)
dec.appendleft(9)
# dec.pop()
d1 = {1:2, 2:3, 5:6, 6:7}
d2 = {3:4, 4:5}
ch_map = collections.ChainMap(d1,d2)

defauld_dict = collections.defaultdict(list)

# Demonstrations functools in python
def lt(a,b):
    return a < b

# Можно делать функцию с фиксированным значением 1 из аргументов
lt_fixet = functools.partial(lt, b = 0)


# Декоратор, который запоминает значение вывода в функции
@functools.lru_cache()
def sum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


# Определяя 2 методы равно и меньше, остальные методы не прийдется дополнительно переопределять
@functools.total_ordering
class Counter():
    def __init__(self, count):
        self.count = count
    def __eq__(self, other):
        return self.count == other.count
    def __lt__(self, other):
        return self.count < other.count


# Модуль iterttols

# itertools.islice - нужна для реализации генератора с доп условиями(начальные значения, до куда идем, шаг)
gen = range(10 )
gen_islice = itertools.islice(gen, 2, 8, 2)


l_1 = [1,2,3]
l_2 = [4,5,6,7,8,9]



if __name__ == '__main__':
    # Класс счетчик- выводит частоту объекта
    print(counter.most_common(1))
    # Двухсторонняя очередь - база
    print(dec)
    # Штука нужна для реализации словаря списков, создание по индексу и пошла жара
    defauld_dict[0].append(213)
    print(defauld_dict)
    # Тут можно объеденять словари и в 1 большой мама дусь объект
    print(ch_map)

    print(lt_fixet(-1))
    start = time.time()
    sum(100)
    print(time.time() - start)

    start = time.time()
    sum(100)
    print(time.time() - start)

    print(Counter(3) >=  Counter(2))

    for i in gen_islice:
        print(i)

    for el1, el2 in itertools.zip_longest(l_1, l_2):
        print(el1, el2)

    print("Compinations itertools:")
    for el1 in itertools.combinations(l_1, 2):
        print(el1)



