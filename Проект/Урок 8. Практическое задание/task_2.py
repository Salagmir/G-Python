"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class my_exception_class(Exception):
    def __init__(self, *args):
        self.txt = args[0] if args else None

    def __str__(self):
        return f"Ошибка - {self.txt}"


try:
    a = int(input("Введите число >>> "))
    b = int(input("Введите делитель >>> "))
    if b == 0:
        raise my_exception_class("Делить на ноль нельзя!")
    print(a // b)
except my_exception_class as err:
    print(err)
