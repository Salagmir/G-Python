"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

list_1 = input("Введите значения в список >>> ").split()
index = 0
for i in range(int(len(list_1) / 2)):
    # range(int(len(list_1) / 2)) Создаёт количисто того сколько раз надо выполнять цыкл
    # Создавая число от количество паар в списке
    list_1[index], list_1[index + 1] = list_1[index + 1], list_1[index]     # Меняет местами a, b = b, a
    index += 2
print(list_1)







