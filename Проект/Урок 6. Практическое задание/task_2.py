"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    asphalt_mass = 25
    thickness_of_the_canvas = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation_of_asphalt_mass(self):
        try:
            a = int(self._length * self._width * self.asphalt_mass * self.thickness_of_the_canvas)
        except TypeError:
            return None
        else:
            return f"{a} кг = {a // 1000} т"


x = Road(20, 5000)
print(x.calculation_of_asphalt_mass())
