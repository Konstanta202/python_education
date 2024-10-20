# defenition FUNCTIONS PYTHON

def phone(model, charge = 100, storage = '120 GB', status = "Workig"):
    if not 0 <= charge <= 100:
        print('Incorrect charge data')
        return
    print(
        f'This {model} is {charge} percent charge.'
          f'It has {storage} storage, current status is {status}'
    )
phone_lumb = ['Iphone']
print(phone(*phone_lumb))
def func_factorial(num):
    if num == 1:
        return 1
    else:
        return num * func_factorial(num-1)

def func(val, mass = None):
    mass = mass or []
    mass.append(val)
    return mass





a = func(1)
print(a)
b = func(3)
print(b,a)
c = func(2)
print(c)

print(a,b,c)

#
# print(medium_num('1 2 3 4'))
# print(func_factorial(5))
#
# phone("Iphone")
