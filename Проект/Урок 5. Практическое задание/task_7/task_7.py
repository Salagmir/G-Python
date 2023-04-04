"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

with open("test.txt", "r", encoding="utf-8") as my_file:
    average_profit_dictionary, average_profit, my_list = {}, 0, []
    for my_line in my_file:
        my_line = my_line.split()
        my_dictionary, revenue, costs = {}, int(my_line[2]), int(my_line[3])
        result = revenue - costs
        if result >= 0:
            average_profit += result
        my_dictionary[my_line[0]] = result
        my_list.append(my_dictionary)
    average_profit_dictionary["average_profit"] = average_profit
    my_list.append(average_profit_dictionary)

with open("test.json", "w") as my_file_2:
    print(my_list, file=my_file_2)
