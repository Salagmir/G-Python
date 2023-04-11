"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, *data):
        my_list = []
        for y in data:
            my_list.append([y])
        self.my_list = my_list

    def __str__(self):
        return str(self.my_list)

    def __add__(self, other):
        return Matrix(self.my_list[0][0] + other.my_list[0][0], self.my_list[1][0] + other.my_list[1][0], self.my_list[2][0] + other.my_list[2][0])


x = Matrix(1, 2, 3)
z = Matrix(1, 2, 3)

print(x)
print(x + z)
