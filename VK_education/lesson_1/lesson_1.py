a = []
a = list()
a = [1,2,3,4,5, "abs", "bve"]
print(a)

#кортеж

b = ()
b = tuple()
b = (1, 3,"abscr")
print(b)


print(a[-len(a)])
print(a[1:6:2]) #1:6 - диапозон 6:2 - это шаг

print(2123 in a, 10 not in a)
q = [1,23,435,34,5,34,5,567,5678,56,7,568,576,8956,48,56,856,8,]
print(min(q), max(q))

g = q + [3,4]
print(g)

c = q * 3
print(c)



p = [1,2,3,4,5,6,7,8,9]
p[2:4] = [-3,-4]
print(p)

del p[1:5]
print(p)

p.append(10)
print(p)

p.extend([1,2,3,4,5,6,7,8,9])
print(p)

p += [11,123,1233,1234,1235,1236]
print(p)

p.insert(0,200)
print(p)


print(p.pop(0))
p.remove(1236 )
print((p))

p.sort()
print(p)
k = p.copy()
p.clear()
print(k,'\n',p)
var1, var2, var3 = ["abs", 23, [1,23,44]]
print(var1,var2,var3)

z = list(range(10))
print(z)

n = [2 ** x for x in z if x % 2 == 0]
print(n)

m = tuple(int(x) for x in "1cj3jdl2" if x.isdigit())
print(m)

str = ["Hello", "Michael", "Gordon"]
jointed = " ".join(str)
print(jointed)

vr = input()
print(round(sum([ + len(x) / len(vr.split()) for x in vr.split()]), 2))


