from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    deq = deque(nums)
    for i in range(n):
        a = deq.pop()
        deq.appendleft(a)
    return list(deq)
#
# if __name__ == '__main__':
#     print(rotate_list([1,2,3,4], 1))
#     print(rotate_list([1, 2, 3, 4], 2))

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)