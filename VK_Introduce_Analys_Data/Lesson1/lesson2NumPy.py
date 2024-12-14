# NumPy
import numpy as np
# NumPy - это библиотека для языка пайтон,
# которая предоставляет высокопроизводительные возможности для работы

# ndarray - это быстрый и гибкий контейнер для хранения больних наборов данных в пайтон
# ndarray.ndim - число осей(измерений) массива
# ndarray.shape - размеры массива, его форма - кортеж натуральных чисел для NxM матриц
# ndarray.size - число всех элементов массива
# ndarray.dtype - объект, описывающий тип элементов массива



data1 = [[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]]
arr1 = np.array(data1)
print(arr1)

print(arr1.ndim)
print(arr1.size)
print(arr1.shape)
print(arr1.dtype)
print(arr1.itemsize)
# создание пустого массива, состоящего из нулей
arrZero = np.zeros(10)
print(arrZero)
# создание массива, состоящего из единиц
arrOne = np.ones((2,2))
print(arrOne)
# создание массива заполненого последовательно от 0 до 14
arrRange = np.arange(15)
print(arrRange)
# linspace - может завать массив с от 0 до числа и определенное количество - например от 0 до 1 и 25 элементов
arrLins = np.linspace(0, 1, 25)
print(arrLins)
# создание единичной матрицы
arrEye = np.eye(3)
print(arrEye)
# операции между массивами и скалярами
print('-'*90)
print("Операции над матрицами")
print("Умножение")
arr = np.array([[1,2,3],[4,5,6]])
print(arr * arr)
print("Вычитание")
print(arr - arr)
print("Деление единицы на матрицу")
print(1 / arr)
print("Возведение в степень")
print(arr ** 3)
print("Рандомные числа")
print("-"*90)
print("Многомерный")
print(np.random.randn(3, 2))
print("Одномерный массив")
print(np.random.randint(0, 1000, 4))

print("-"*90)
print("Индексирование")

print(np.arange(15)[8:12])
print("*"*90)
array2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2D[2])
print("-"*90)
print("Интересные дела")

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
arrBool = names == 'Bob'
print(arrBool)
mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(names[mask])

print("-"*90)
print("Математические и статические операции")

arr_ = np.random.randn(5,4)
print(arr_)
print(f"SHAPE: {arr_.shape}")

print(f"ARR MEAN: {arr_.mean()}")
print(f"ARR SUM: {arr_.sum()}")
print(f"ARR MAX: {arr_.max()}")
print(f"SUM OSI: {arr_.sum(axis = 0)}")
print("-"*90)
print("TASK")
arr = np.arange(10,500)
#arr = arr ** 2 - 234
print((arr ** 2 - 234).sum())

