"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

try:
    revenue = int(input("Ваша выручка >>> "))
    cost = int(input("Ваши издержки >>> "))
except ValueError:
    print("Не число")
    exit(0)

profit = revenue - cost
profitability = profit / revenue

if profit > 0:
    print(f"Финансовый результат - прибыль. Ее величина: {profit}$ Рентабельность {profitability}$")
    try:
        staff = int(input("Численность сотрудников фирмы >>> "))
    except ValueError:
        print("Не число")
        exit(0)
    if staff > 0:
        profitability_staff = profit / staff
        print(f"Один сотрудник вам приносит {profitability_staff}$")
    else:
        print("Ошибка! Сотрудников меньше 1")
elif revenue == cost:
    print(f"Рентабельность {profit}$")
    exit(0)
else:
    print(f"Убыток {profit}$")
    exit(0)
