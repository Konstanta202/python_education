str = str.split(input())
for i in map(lambda x: x * x if x % 2 == 1 else -x, range(int(str[0]),int(str[1]),int(str[2]))): print(i)
