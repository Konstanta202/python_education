a = dict()

for key, value in a.items():
    print(key, value)

f = {x : 2 ** x for x in range(10)}

for key, value in f.items():
    print(key,"-",value)

g = {k : v for k, v in f.items() if k % 2 == 1}
print(g)
print(1 in g or 2 in g)


print(f.get(2, -1))

p = {'one' : 1, 'two': 2, 'three': 3}
k = {'one' : -1, 'two': -2, 'four': -4}

p.update(k)
print(p)
p.update([('one',1) ,( 'two',2)], three = -3)
print(p)

del p['one']
print(p)
val = p.pop('tre o', None)
print(val)

# print(j)
# print(j < {1,23,123,12,23,534,4,5,6,7,8,9,76,5,433,123,5,7})


j = {1,2,3,4,5,67,78,23}
g = {1,2,3,4,5,98,97,96,65,66}
print("Move set fuctrion for second set")
print(j | g)
print(j & g)
print(j - g)
print(g - j)
print(j ^ g)


j.discard(67)
g.clear()
# frozenset - неизменяемое множество, можем использовать его в качестве ключа