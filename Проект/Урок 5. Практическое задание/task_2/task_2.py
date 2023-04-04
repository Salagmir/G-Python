"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("test.txt", "r", encoding="utf-8") as x:
    a = x.readlines()
    print("Строк -", len(a))
    print("Слов -", sum([len(i) for i in [c.split() for c in a]]))
