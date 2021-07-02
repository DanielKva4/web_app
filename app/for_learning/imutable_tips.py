from functools import partial
import time
from datetime import datetime


# x = [3, 5, 6]
# def immut(a):
#     a[2] = 7
# immut(x)
# print(x)


# 1. Написать функцию которая будет распаковывать цифры 7 и 6 в переменные x и y из списка
# ls = [4,[7,8],6]    Использовать unboxing.


# ls = [4, [7, 8], 6]
# _, (a, _), b = ls
# print(a, b)


# 2. Написать функцию которая будет бежать for-ом по списку  ls = [ (3, [9, 1]), [(23,43), [5, 4]] ]
# и суммировать элементы 9 и 5 используя unboxing.


# ls2 = [(3, [9, 1]), [(23, 43), [5, 4]]]
# result = 0
# for (_, (a, _)) in ls2:
#     result += a
#     print(result)


# 1. Сделать генератор который принимает на вход число x, пусть x = 5, и возвращает 5 разных простых чисел.




def true_numbers(a, b):
    x = range(a, b)
    for i in x:
        if i % 2 == 0:
            print(i)
    return 'aboba'


partial_fn = partial(true_numbers, 1)
print(partial_fn(10))


# Решить ее потом вместе с колей
def simple(a, ls):
    found_numbs = 0
    last_prime = 1
    while found_numbs != a:
        prime = True
        for y in range(2, last_prime):
            if last_prime % y == 0:
                prime = False
                break
        if prime:
            found_numbs += 1
            yield last_prime
        last_prime += 1


# def lazy_map(fn, ls):
#     for x in ls:
#         y = fn(x)
#


start = datetime.now()
generator = simple(100)
print(next(generator))
print(next(generator))
print('Программа выполнена за ' + str((datetime.now() - start).total_seconds()) + ' секунд')
