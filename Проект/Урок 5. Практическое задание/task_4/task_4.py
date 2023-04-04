"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("test.txt", "r", encoding="utf-8") as my_file:
    counter = 0
    average_income = 0
    for x in my_file:
        salary = float(x.split()[1])
        if salary >= 20000:
            print(x)
        average_income += salary
        counter += 1
    average_income = average_income // counter
    print(f"Cредняя величина дохода сотрудников {average_income}")
