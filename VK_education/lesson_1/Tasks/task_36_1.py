def filter(func, seq):
    for item in seq:
        if func(item):
            yield item


func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)


   # lambda x: x > 0
   # (1, 2, 0, 3, -1, -2, 5)