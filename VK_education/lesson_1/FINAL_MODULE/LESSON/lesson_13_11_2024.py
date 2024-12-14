# import collections
# import functools
# import time
# import itertools
# # Demonstrations Collections in Python
# l1 = [1, 1, 3, 3, 3, 6, 7, 8, 8]
# counter = collections.Counter(l1)
# dec = collections.deque(l1)
# dec.append(4)
# dec.appendleft(9)
# # dec.pop()
# d1 = {1:2, 2:3, 5:6, 6:7}
# d2 = {3:4, 4:5}
# ch_map = collections.ChainMap(d1,d2)
#
# defauld_dict = collections.defaultdict(list)
#
# # Demonstrations functools in python
# def lt(a,b):
#     return a < b
#
# # Можно делать функцию с фиксированным значением 1 из аргументов
# lt_fixet = functools.partial(lt, b = 0)
#
#
# # Декоратор, который запоминает значение вывода в функции
# @functools.lru_cache()
# def sum(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum
#
#
# # Определяя 2 методы равно и меньше, остальные методы не прийдется дополнительно переопределять
# @functools.total_ordering
# class Counter():
#     def __init__(self, count):
#         self.count = count
#     def __eq__(self, other):
#         return self.count == other.count
#     def __lt__(self, other):
#         return self.count < other.count
#
#
# # Модуль iterttols
#
# # itertools.islice - нужна для реализации генератора с доп условиями(начальные значения, до куда идем, шаг)
# gen = range(10 )
# gen_islice = itertools.islice(gen, 2, 8, 2)
#
#
# l_1 = [1,2,3]
# l_2 = [4,5,6,7,8,9]
#
#
#
# if __name__ == '__main__':
#     # Класс счетчик- выводит частоту объекта
#     print(counter.most_common(1))
#     # Двухсторонняя очередь - база
#     print(dec)
#     # Штука нужна для реализации словаря списков, создание по индексу и пошла жара
#     defauld_dict[0].append(213)
#     print(defauld_dict)
#     # Тут можно объеденять словари и в 1 большой мама дусь объект
#     print(ch_map)
#
#     print(lt_fixet(-1))
#     start = time.time()
#     sum(100)
#     print(time.time() - start)
#
#     start = time.time()
#     sum(100)
#     print(time.time() - start)
#
#     print(Counter(3) >=  Counter(2))
#
#     for i in gen_islice:
#         print(i)
#
#     for el1, el2 in itertools.zip_longest(l_1, l_2):
#         print(el1, el2)
#
#     print("Compinations itertools:")
#     for el1 in itertools.combinations(l_1, 2):
#         print(el1)
import math
from scipy.stats import norm

def solution(arrX: list, arrVi:list, x:float) -> list:
    result: float = 0.0
    result_full = []
    for i in range(len(arrX)):
        result += arrVi[i] * (arrX[i] - x) ** 2
        print(result)
    result = result / 200

    result_full.append(result)
    result_full.append(math.sqrt(result))
    return result_full

def solution_central_M3(arrX: list, arrVi:list, x:float) -> float:
    result: float = 0.0
    for i in range(len(arrX)):
        result += arrVi[i] * (arrX[i] - x) ** 3
    result = result / 200
    return result


def invers(arrX: list, arrY:list) -> int:
    inversions = 0
    for x in arrX:
        for y in arrY:
            if x > y:
                inversions += 1
    return inversions




# Исходные данные

if __name__ == '__main__':

    arrx = [1332.0, 1315.0, 1326.0, 1341.0, 1313.0, 1299.0, 1321.0, 1322.0, 1336.0, 1303.0, 1335.0, 1322.0, 1318.0, 1312.0, 1329.0, 1312.0, 1301.0, 1313.0, 1306.0, 1313.0]

    ARRX = [861.3, 817.9, 808.2, 808.3, 839.3, 722.5, 813.3, 805.7,
              790.3, 863.6, 817.1, 797.2, 810.0, 758.2, 820.3, 893.2,
              840.1, 900.3, 819.4, 831.9]

    ARRY = [794.7, 861.8, 783.4, 860.8, 824.0, 874.1, 796.8,
                 838.9, 808.9, 835.1, 810.2, 866.3, 844.7, 853.9,
                 825.2, 793.6, 776.3, 812.0, 847.4, 789.7]



    arry = [1324.0, 1310.0, 1322.0, 1318.0, 1294.0, 1312.0, 1314.0, 1345.0, 1301.0, 1320.0, 1321.0, 1326.0, 1334.0, 1310.0, 1310.0, 1296.0, 1333.0, 1319.0, 1303.0, 1312.0]
    x_delta = 6.4
    x_begin = 1283.20
    x_chert = 1317.12
    arrX = []
    arrV = [1, 3, 14, 16, 38, 40, 31, 30, 15, 7, 5]
    for i in range(11):
        arrX.append(x_begin + i * x_delta)

    arrS = solution(arrX, arrV, x_chert)
    arrS_ = arrS[1]

    arrM3 = solution_central_M3(arrX, arrV, x_chert)
    print('*'*90)

    print(arrS_)
    arrS_ = arrS_ ** 4
    print(f'{arrM3=}')
    res = arrM3 / arrS_ - 3
    print(round(res,4))

    x1 = 1302.4
    x2 = 1328.0

    # Находим z1 и z2
    z1 = norm.ppf(0.17)
    z2 = norm.ppf(0.865)

    # Вычисляем sigma
    sigma = (x2 - x1) / (z2 - z1)

    # Вычисляем m
    m = x1 - z1 * sigma
    #  m = 1314.274 sig = 12.443
    print(f"m = {m:.5f}, sigma и = {sigma:.5f}")

    from scipy.stats import chi2

    print("-"*100)
    # df - число степеней свободы
    df = 20
    alpha = 0.05  # Уровень значимости 5%
    # Найти критическое значение
    chi2_critical = chi2.ppf(1 - alpha, df)
    print(chi2_critical)
    print('+'*90)
    print(invers(arrx,arry))
    print(invers(ARRX,ARRY))