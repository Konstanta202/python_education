str = input()
str = str.lower()
words = str.split()
three = dict()
for word in words:
    if word in three:
        three[word] += 1
    else:
        three[word] = 1
a = ''
for k, v in three.items():
    if v == max(three.values()):
        a = k
print(a, max(three.values()))