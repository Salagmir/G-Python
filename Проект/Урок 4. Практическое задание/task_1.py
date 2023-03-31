"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv


def payroll_calculation(output_in_hours, rate_per_hour, prize):
    return (output_in_hours * rate_per_hour) + prize


print(payroll_calculation(int(argv[1]), int(argv[2]), int(argv[3])), "$")
