# Необходимо написать программу, которая будет считывать со стандартного ввода положительное
# целое число – порядковый номер 1 <= n <= 30, и выводить n-е по счету число Фибоначчи.
# Числа Фибоначчи это последовательность чисел такая, что каждое следующее число это сумма
# двух предыдущих. Первое и второе числа Фибоначчи это числа 1. То есть первые два числа это 1 и 1,
# третье число это 2 (сумма первого и второго), четвертое число это 3 (сумма второго и третьего), пятое – 5,
# шестое – 8 и так далее. Нужно написать этот код с помощью рекурсии.
#
# * При отладке кода вы можете заметить, что уже на не очень больших числах около 40 код
# начинает долго выполняться. Это из-за того что число операций растет экспоненциально, то есть
# очень быстро, при этом большинство вычислений повторяется. Это можно решить“закэшировав” данные,
# а именно завести глобальную переменную-словарь, а в самой рекурсии проверять нет ли уже в этом словаре
# вычисленного значения для нужного вам порядкового номера. Если есть, то взять его в качестве результата, а
# если нет, то вычислить его также с помощью рекурсии и положить в этот словарь.


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
num = input()
print(fibonacci(int(num)))


def ff(*, he = 100, w = 100):
    return he*w

print(ff(he = 10, w = 20))