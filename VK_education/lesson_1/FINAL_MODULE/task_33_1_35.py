from collections import defaultdict
from typing import List, Tuple

import datetime

print(datetime.date.today())


def fill_specializations(specializations: List[Tuple[str, str]]):
    dict_default = defaultdict(list)
    for specialization in specializations:
        dict_default[specialization[0]].append(specialization[1])

    return dict(dict_default)

def calculate(R1,R2,R3,R4) -> list:
    n = 5 + 2 * R1 * (4 / R2 - 1 / R4)
    z1 = round( ((-20 + 5 + 2 * R1 * (4 / R2 - 1 / R4)) / 4  -1) ,4)
    z2 = round( ((-0.8 + 1 - 0.03 * R4) / 0.16 - 1) ,4)
    z3 = round( ((20 - 20 / R1 - 10 / R2) / 4 - 1) ,4)
    z4 = round( ((15 - 0.5 - (0.1 * R2) / R4 - R2 * (6 + (0.1 * n)) - (7/(8 + 3 * R3)) ) / 3 - 1) ,4)
    z5 = round( ((-1.5 + (10 * R2) / R1) / 0.3) , 4)
    return [z1,z2,z3,z4,z5]
#
if __name__ == '__main__':
    k = 25

    Ar = 1 + 6 / (k + 6)
    print("A")
    print(calculate(Ar,Ar,Ar,Ar))

    print("B")
    print(calculate(0.5,0.5,Ar,0.1))


    # specs = [('Sales', 'John Doe'), ('Sales', 'Martin Smith'), ('Accounting', 'Jane Doe'),
    #          ('Marketing', 'Elizabeth Smith'), ('Marketing', 'Adam Doe')]
    # print(fill_specializations(specs))

# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
