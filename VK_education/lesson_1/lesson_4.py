# defenition FUNCTIONS PYTHON





# Аннотации к функции делаются при помоши """" аннотация """
def phone(model, charge = 100, storage = '120 GB', status = "Workig"):

    """
    Тут происходит описание аннотации,например,

    : param model: type String, you need put this param for called function
    """

    if not 0 <= charge <= 100:
        print('Incorrect charge data')
        return
    print(
        f'This {model} is {charge} percent charge.'
          f'It has {storage} storage, current status is {status}'
    )


#Чтобы вызвать аннотацию, необходимо написать help(name_function)

help(phone)



#  Можно также деалть явное определение типа при вызове функции
#  Example:  def phone(model:str, charge:int = 100, storage = '120 GB', status = "Workig"):

def phone(model:str, charge:int = 100, storage = '120 GB', status = "Workig"):
    print(model, charge, storage, status)


# Если ты крутой программист, и ты пишешь крутые штуки, но на данный момент сроки горят и тебе необходимо реализовать
# что то круто, но ты не придумал как реализовать функцию для этого, то выход есть мой дорогой друг,
# тебе просто необходимо записать в функции ключевое слово "pass" или же сделать крутой мув и написать "..."

def super_func(model:str, charge:int = 100, storage = ''):
               pass


# в переменную можно записать функцию(ахереть)

copu_phone = phone


l_func = lambda x: 2 ** x
print(l_func(3))



a = [1,2,3,4,5]
b = sorted(a, key = lambda x: -x)
print(b)


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n -1)
print(factorial(5))



def factorial_v2(n):
    val = 1
    for i in range(1, n+1):
        val *=i
    return val
print(factorial_v2(5))