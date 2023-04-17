"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class my_date:
    day_month_year = "11.04.2023"

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"

    @classmethod
    def transformation(cls):
        my_list = cls.day_month_year.split('.')
        return my_date(int(my_list[0]), int(my_list[1]), int(my_list[2]))

    @staticmethod
    def number_validation(number):
        try:
            number = number.split(".")
            if 1 <= int(number[0]) <= 12 and 2020 <= int(number[1]) <= 2025:
                return True
            else:
                return False
        except ValueError:
            return False


my_method = my_date
print(my_method.transformation())
print(my_method.number_validation("11.2023"))
