def medium_num(str):
    med = 0
    arr_str = str.split()
    for i in arr_str:
        med += int(i)
    return round(med/len(arr_str),2)

arr_1 = list()
str = input()
while(str != ''):
    arr_1.append(str)
    str = input()
for i in range (len(arr_1)):
    print(medium_num(arr_1[i]))