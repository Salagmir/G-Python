"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class my_exception_class(Exception):
    def __init__(self, *args):
        self.txt = args[0] if args else None

    def __str__(self):
        return f"Ошибка - {self.txt}"


my_list = []
while True:
    number = input("Введите число или # для выхода >>> ")
    if number == "#":
        break
    try:
        if not number.isdigit():
            raise my_exception_class("Не првельный тип данных")
        my_list.append(int(number))
    except my_exception_class as err:
        print(err)
print(my_list)
