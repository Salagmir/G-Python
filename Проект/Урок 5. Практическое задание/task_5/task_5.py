"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("test.txt", "w", encoding="utf-8") as my_file:
    print(12, 123, 1242, 356, 456, 1623, 456, 12323, 56, 144423, file=my_file)

with open("test.txt", "r", encoding="utf-8") as my_file:
    my_list = 0
    for x in my_file.read().split():
        my_list += int(x)
    print(my_list)
