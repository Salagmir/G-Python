"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return "Уникальное сообщение 1"


class Pencil(Stationery):
    def draw(self):
        return "Уникальное сообщение 2"


class Handle(Stationery):
    def draw(self):
        return "Уникальное сообщение 3"


x_1 = Stationery(None)
x_2 = Pen("Ручка")
x_3 = Pencil("Карандаш")
x_4 = Handle("Ручка")

print(x_1.draw())
print(x_2.draw())
print(x_3.draw())
print(x_4.draw())
