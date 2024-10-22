def repeat_deco(n=1):
    def deco(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                val = func(*args, **kwargs)
            return val
        return wrapper
    return deco


@repeat_deco(3)
def my_func():
    print("Hello")


# code = []
# while data := input():
# code.append(data)
# code = "\n".join(code)
# exec(code)

my_func()
@repeat_deco(3)
def add(seq, val):
    seq.append(val)
    return seq
print(add([], 1))