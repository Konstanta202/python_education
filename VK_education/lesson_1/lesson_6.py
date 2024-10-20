# ДЕКАРАТОРЫ КАК СМЫСЛ ЖИЗНИ
# КРАТКОЕ ИСПОЛЬЗОВАНИЕ ДЕКАРАТОРА ПРОИСХОДИТ, КОГДА МОЛОДОЙ ЧЕЛОВЕК ИСПОЛЬЗУЕТ К ФУНКЦИИ ТЕГ @decarator_name
# ЕСЛИ ИСПОЛЬЗОВАТЬ НЕСКОЛЬКО ДЕКАРАТОРОВ, ТО ОНИ БУДУТ ВЫПОЛНЯТЬСЯ СНИЖУ ВВЕРХ
def decarator_func1(func):
    print('Start decarator ')
    def wrapper():
        print('Start1')
        func()
        print('End1')
    print('End decarator ')
    return wrapper


@decarator_func1
def my_func():
    print('Hello world')

print('-------------------')
my_func()
print('-------------------')




def decarator_func2(func):
    print('Start decarator ')
    def wrapper(*args, **kwargs):
        print('START WRAPPER')
        func(*args, **kwargs)
        print('END WRAPPER')
    print('End decarator ')
    return wrapper

@decarator_func2
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
phone('Iphone', charge = 6, storage = '200 GB', status = 'SLEEP')