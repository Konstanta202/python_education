import itertools
import string
import pandas as pd
import os

if __name__ == '__main__':
    df = pd.DataFrame(data=[
        ["Rock","Heavy PAPER","ENGLISH"],
        ["POP", "BIBER", "ENGLISH"],
        ["Rock", "Ramshtain", "Germany"],
        ["Rock", "SOAD", "ARMENIA"]
    ], columns=['Type music', 'Group/Solist',"Country"])
    print(df)








def find_first_words(path):
    list_result = []
    with open(path, 'r+') as file:
        for line in file:
            if line == '\n':
                list_result.append('')
            else:
                line_stripped = list(line.split())
                list_result.append(line_stripped[0])

    return list_result


# папка и файлы, которые мы создадим с помощью Python, и с которыми будем работать


# print(find_first_words('simple_file_with_empty_lines.txt'))


class StringManipulator:
    """Docstring of StringManipulator"""
    import string
    category = 'Manipulator'

    def __init__(self, original):
        self.phrase = original

    def reverse_words(self):
        """разворачивает атрибут phrase наоборот"""
        # words - список слов, разделённых пробелами
        words = self.phrase.split()
        # reversed меняет порядок элементов в списке наоборот
        self.phrase = ' '.join(reversed(words))

    def make_title(self):
        words = self.phrase.split()
        self.phrase = string.capwords(' '.join(reversed(words)), ' ')
        # self.phrase = ' '.join(reversed(self.phrase))

        # наполните этот метод
        # ниже видно, что он переводит, например, строку "cOOL pyThON" в "Python Cool"
        # чтобы поменять местами порядок слов, тут можно воспользоваться методом выше

    def get_manipulated(self):
        """возвращает атрибут phrase после всего, что мы с ним сделали с помощью других методов"""
        return self.phrase





#
# magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)
#
# sum_of_values = 0
# for value in magic_dict.values():
#     if isinstance(value,(int,float)):
#         sum_of_values = sum_of_values + value
# print(sum_of_values)
#
#
# numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# #%%
# def number_indicator(number):
#     print(number)
#     if number % 5 == 0:
#         if number % 2 == 0:
#             return 'five even'
#         else:
#             return 'five odd'
#     elif number % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# # Ваше решение
# my_list = [number_indicator(x) for x in numbers]
# print(my_list)
# a = list(filter(lambda x: x % 2 == 0, numbers))
# print(a)
# str = '123,123,123,434'
# str1 = str.split()
# print(str1)
#
# a = 300
# b = a
# b = b - 300
# print(a,b)
#
#
#
# result = 'asd' + '\n' + 'asd'
# asd = []
# for i in range(10) :
#     asd.append(str(i))
# print(asd)
#
# print(result)

# #кортеж
#
# b = ()
# b = tuple()
# b = (1, 3,"abscr")
# print(b)
#
#
# print(a[-len(a)])
# print(a[1:6:2]) #1:6 - диапозон 6:2 - это шаг
#
# print(2123 in a, 10 not in a)
# q = [1,23,435,34,5,34,5,567,5678,56,7,568,576,8956,48,56,856,8,]
# print(min(q), max(q))
#
# g = q + [3,4]
# print(g)
#
# c = q * 3
# print(c)
#
#
#
# p = [1,2,3,4,5,6,7,8,9]
# p[2:4] = [-3,-4]
# print(p)
#
# del p[1:5]
# print(p)
#
# p.append(10)
# print(p)
#
# p.extend([1,2,3,4,5,6,7,8,9])
# print(p)
#
# p += [11,123,1233,1234,1235,1236]
# print(p)
#
# p.insert(0,200)
# print(p)
#
#
# print(p.pop(0))
# p.remove(1236 )
# print((p))
#
# p.sort()
# print(p)
# k = p.copy()
# p.clear()
# print(k,'\n',p)
# var1, var2, var3 = ["abs", 23, [1,23,44]]
# print(var1,var2,var3)
#
# z = list(range(10))
# print(z)
#
# n = [2 ** x for x in z if x % 2 == 0]
# print(n)
#
# m = tuple(int(x) for x in "1cj3jdl2" if x.isdigit())
# print(m)
#
# str = ["Hello", "Michael", "Gordon"]
# jointed = " ".join(str)
# print(jointed)
#
# vr = input()
# print(round(sum([ + len(x) / len(vr.split()) for x in vr.split()]), 2))
#
#
