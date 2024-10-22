def cache_deco(func):
    cache = dict()
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper


@cache_deco
def fib(k):
    if k <=2:
        return 1
    return fib(k-1) + fib(k-2)


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
print(code)
exec(code)



# test function
# print(fib(300))