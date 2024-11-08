from typing import Type


def cache_deco(func):
    cache = dict()
    def wrapper(*args):
        if cache.get(args) is None:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def solution(func_map, func_filter, data):
    filter_data = (item for item in data if func_filter(item))
    mapped_data = (func_map(item) for item in filter_data)
    for index, item in enumerate(mapped_data):
        if index % 2 == 0:
            yield item;


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
