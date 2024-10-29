from typing import Type


def cache_deco(func):
    cache = dict()
    def wrapper(*args, **kwargs):
        if cache.get(args) is None:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper()


def solution(func_map, func_filter, data):
    res = []
    for i in data:
        if func_filter(i):
            res.append(func_map(i))
            yield i


def calc():
    count = 0
    @cache_deco
    def calc_(x):
        nonlocal count
        count += 1
        print("Call:", count)
        return x
    return calc_

if __name__ == '__main__':
    for i in (solution(calc(),lambda x: x % 2 == 1, (1,2,3,4,5,6,7,8,9,10))):
        print(i)

