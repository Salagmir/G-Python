"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

with open("test.txt", "r", encoding="utf-8") as my_file:
    substitution = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    my_list = []
    for i in my_file:
        my_line = i.split()
        x = my_line.pop(0)
        my_line.insert(0, substitution[x])
        my_line = " ".join(my_line)
        my_list.append(my_line)
        with open("test_2.txt", "w", encoding="utf-8") as my_file_2:
            for x in my_list:
                print(x, file=my_file_2)
