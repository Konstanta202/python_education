a = int(input())
def f():
    global a
    a += 10
f()
print(a)


def g():
    b = int(input())
    def h():
        nonlocal b
        b += 10
    h()
    print(b)

if __name__ == "__main__" :
    print('this is main')
    g()

