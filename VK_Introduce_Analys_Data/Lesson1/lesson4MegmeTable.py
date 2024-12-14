import pandas as pd

raw_data = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}
df_a = pd.DataFrame(raw_data, columns=['subject_id', 'first_name', 'last_name'])
df_a.index = [0,1,2,3,4]
print(df_a)

raw_data2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Blawner', 'Brice', 'Btisan']
}

df_b = pd.DataFrame(raw_data2, columns=['subject_id', 'first_name', 'last_name'])
print('*'*90)
df_a.index = [2,3,4,5,6]
print(df_b)
print('*'*90)
raw_data3 = {
    'subject_id': ['1', '2', '3', '4', '5', '6','7','8','9', '10', '11'],
    'test_id': [51,15,15,61,61,16,14,15,1,61,16]
}

df_n = pd.DataFrame(raw_data3, columns=['subject_id', 'test_id'])
print(df_n)
print('*'*90)
print("Method concat")
# Конкат как правило используется для объеденения таблиц по вертикальной или горизонтальной оси

df_new = pd.concat([df_a, df_b], axis = 0)
print(df_new)
df_new2 = pd.concat([df_a, df_b], axis = 1)
print(df_new2)

# Concat используется для объеденения в таблицах только тех, которые есть там и там "inner"
df_new3 = pd.concat([df_a, df_b], axis = 1, join = 'inner')
print(df_new3)

# Append - частный случай Concat с параметрами (axis = 0, join = 'outer')
#print(df_a._append(df_b))
print('-'*90)
# Join основан на объеденении таблиц через индексы (способ объеденения указывается с помощью параметра how
# [left , right, inner, outer]
print(df_a.join(df_b, rsuffix='__right_table__', how = 'left'))


# merge используется для объеденения таблиц по любым колонкам с помощью методов left_on and right_on

print(pd.merge(df_new, df_n, on = 'subject_id'))




