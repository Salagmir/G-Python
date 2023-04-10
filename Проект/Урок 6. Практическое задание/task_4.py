"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import randint


class Car:
    def __init__(self, name, color, speed, is_police=None):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, where):
        return f"Машина повернула на {where}"

    def show_speed(self):
        return f"Скорость {randint(0, self.speed)}"


class TownCar(Car):
    def __str__(self):
        return "Это городской автомобиль"

    def show_speed(self):
        x = randint(0, self.speed)
        if x > 60:
            return f"превышениe скорости на {x - 60}"
        else:
            return f"Скорость {x}"


class SportCar(Car):
    def __str__(self):
        return "Это спортивный автомобиль"


class WorkCar(Car):
    def __str__(self):
        return "Это рабочая машина"

    def show_speed(self):
        x = randint(0, self.speed)
        if x > 40:
            return f"превышениe скорости на {x - 40}"
        else:
            return f"Скорость {x}"


class PoliceCar(Car):
    def __str__(self):
        return "Это полицейская машина"


Car_1 = TownCar("1", "Чёрный", 90, False)
Car_2 = SportCar("2", "Красный", 120, False)
Car_3 = WorkCar("3", "Жёлтый", 60, False)
Car_4 = PoliceCar("4", "Синий", 120, True)

print(Car_1)
print(f"Имя - {Car_1.name}\nЦвет - {Car_1.color}\n{Car_1.show_speed()}")
