# Представьте, что у вас есть словарь с ключами и их частотами (то есть насколько часто встречался каждый ключ)
# в качестве значений. Напишите функцию make_most_common_keys, которая принимает словарь частот и выводит
# отсортированный (например через функцию sorted) по убыванию частот (то есть значений ключей) список ключей.


from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    d1 = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    result = list(d1.keys())
    return result





if __name__ == '__main__':
    code = []
    while data := input():
        code.append(data)
    code = "\n".join(code)
    exec(code)






