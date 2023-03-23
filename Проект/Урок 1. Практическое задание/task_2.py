"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

try:
    my_time = int(input("Введите время в секундах >>> "))

    my_time = my_time % (24 * 3600)

    hour = my_time // 3600

    minute = my_time % 3600 // 60

    second = my_time % 60

    print(f"{hour}:{minute}:{second}")

except ValueError:
    print("Не число")
