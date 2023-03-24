"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-1] + my_list[-2]


def my_func_2(a, b, c):
    return a + b + c - min([a, b, c])


print(my_func(3, 2, 1))
print(my_func_2(3, 2, 1))
