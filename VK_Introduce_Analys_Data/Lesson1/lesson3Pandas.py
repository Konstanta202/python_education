import pandas as pd
import numpy as np

print("Start Work")
print("*"*90)
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)

my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['A', 'B', 'C', 'D', 'E', 'G'])
print(my_series2)

mask = my_series > 7
print(mask)
print(my_series[mask])

# Серию можно задавать как словарь

my_series3 = pd.Series({'a':5,'b':6,'c':7,'d':8})
print(my_series3)
# можно переопределять название серии или индексов
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
print(my_series3)

# DataFrame -
df = pd.DataFrame({'city':['San Francisco', 'Mexico', 'New York', 'China'],
                   'delivery_time': [25,29,32,30],
                   'price':[100,200,300,400]
                   })
print(df)
print(df.delivery_time)

# сохранение в разные виды файлов от тхт до csv
df.to_csv('output.sql')

# доступ к строкам по индексу возможен несколькими способами:
#   .loc - используется для доступа по строковой метке
#   .iloc - используется для доступа по числовому значению (начиная от 0)
print(df)
print(df.loc[0])
print('*'*90)
# можно сразу обращаться и к индексу и к колонке
print(df.loc[[0,1], 'price'])

# СНАЧАЛА СТРОКА А ПОТОМ КОЛОНКА
print('*'*90)
print(df[df.delivery_time > 30][['city', 'price']])
print('*'*90)
print("Создание новой колонки на основе старой")
df['delivery_time_hours'] = df['delivery_time'] / 60
print(df)
print(df.drop('delivery_time', axis=1))

# Вытаскивает n самых больших показателей из колонки - нет нужны в сортировке
print("Вытаскивание n самых больших показателей")

df.nlargest(1, ['price'])
print('-'*90)
print("read for file csv")
df_read = pd.read_csv(
    '/Users/konstantineskalisusov/PycharmProjects/Education/VK_Introduce_Analys_Data/Lesson1/orders.csv', sep = ',')
#print(df_read)
print(len(df_read['city_id'].unique()))

print(len(df_read[df_read.spec == "Рыба"]['vendor_id'].unique()))

print(len(df_read.select_dtypes(include = ['float64']).columns))

print(len(df_read[(df_read.vendor_id == 40065) & (df_read.successful_orders < 20)]['date'].unique()))

