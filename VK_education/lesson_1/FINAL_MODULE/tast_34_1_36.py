from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    result = list()
    for el1, el2 in zip_longest(values_list_1, values_list_2):
        if el1 == None:
            f = (1, el2)

        elif el2 == None:
            f = (el1, 1)
        else:
            f = (el1, el2)
        result.append(f)
    return result

#
code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# if __name__ == '__main__':
#     print(fill_missing_values([1, 2, 3], [2, 3, 4, 5]))
#     pass