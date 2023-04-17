"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class warehouse:

    shelving = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None]]

    @classmethod
    def reception(cls, shelf, shelf_space, equipment):
        if cls.shelving[shelf][shelf_space] is None:
            cls.shelving[shelf][shelf_space] = equipment
            return True
        else:
            return False

    @classmethod
    def transfer(cls, shelf, shelf_space, company_division):
        if cls.shelving[shelf][shelf_space] is None:
            return False
        else:
            cls.shelving[shelf][shelf_space] = None
            return True


class office_equipment:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour


class printer(office_equipment):
    def __init__(self, print_color, model, colour):
        super().__init__(model, colour)
        self.print_color = print_color

    def __str__(self):
        return f"Модель {self.model} - Тип печати {self.print_color}"


class scanner(office_equipment):
    def __init__(self, speed_operation, model, colour):
        super().__init__(model, colour)
        self.speed_operation = speed_operation

    def __str__(self):
        return f"Модель {self.model} - Скорость операции {self.speed_operation}"


class xerox(office_equipment):
    def __init__(self, the_speed_of_photocopying, model, colour):
        super().__init__(model, colour)
        self.the_speed_of_photocopying = the_speed_of_photocopying

    def __str__(self):
        return f"Модель {self.model} - скорость ксерокопирования {self.the_speed_of_photocopying}"


my_warehouse = warehouse

while True:
    choice = input("Хотите дабавить оргтехнику на склад [y/n] >>> ")
    if choice == "y":
        while True:
            print("1 - Принтер\n2 - Сканер\n3 - Ксерокс\n4 - Назад")
            try:
                choice = int(input("Выберите оргтехнику >>> "))
            except ValueError:
                print("Ошибка ввода!\nПопробуйте её раз!")
            else:
                if choice == 1:
                    model = input("Введите модель принтера >>> ")
                    colour = input("Введите цвет принтера >>> ")
                    print_color = input("Введите цвет печати принтера >>> ")
                    my_printer = printer(model=model, colour=colour, print_color=print_color)
                    while True:
                        try:
                            shelf = int(input("Введите номер полки 1-4 >>> "))
                            if 1 <= shelf <= 4:
                                shelf_space = int(input("Введите место хранения 1-3 >>> "))
                                if 1 <= shelf_space <= 3:
                                    quantity = int(input("Введите количество для хранения >>> "))
                                    my_reception = my_warehouse.reception(shelf-1, shelf_space-1,
                                                                          {"Принтер": my_printer,
                                                                           "Количество": quantity})
                                    if my_reception is True:
                                        print("На склад убранно")
                                        break
                                    elif my_reception is False:
                                        print("Место занято")
                                else:
                                    print("Нет такого места")
                            else:
                                print("Нет такой полки")
                        except ValueError:
                            print("Ошибка ввода!\nПопробуйте её раз!")
                elif choice == 2:
                    model = input("Введите модель сканера >>> ")
                    colour = input("Введите цвет сканера >>> ")
                    speed_operation = input("Введите скорость операции сканера >>> ")
                    my_printer = scanner(model=model, colour=colour, speed_operation=speed_operation)
                    while True:
                        try:
                            shelf = int(input("Введите номер полки 1-4 >>> "))
                            if 1 <= shelf <= 4:
                                shelf_space = int(input("Введите место хранения 1-3 >>> "))
                                if 1 <= shelf_space <= 3:
                                    quantity = int(input("Введите количество для хранения >>> "))
                                    my_reception = my_warehouse.reception(shelf - 1, shelf_space - 1,
                                                                          {"сканер": my_printer,
                                                                           "Количество": quantity})
                                    if my_reception is True:
                                        print("На склад убранно")
                                        break
                                    elif my_reception is False:
                                        print("Место занято")
                                else:
                                    print("Нет такого места")
                            else:
                                print("Нет такой полки")
                        except ValueError:
                            print("Ошибка ввода!\nПопробуйте её раз!")
                elif choice == 3:
                    model = input("Введите модель ксерокса >>> ")
                    colour = input("Введите цвет ксерокса >>> ")
                    the_speed_of_photocopying = input("Введите скорость ксерокопирования >>> ")
                    my_printer = xerox(model=model, colour=colour, the_speed_of_photocopying=the_speed_of_photocopying)
                    while True:
                        try:
                            shelf = int(input("Введите номер полки 1-4 >>> "))
                            if 1 <= shelf <= 4:
                                shelf_space = int(input("Введите место хранения 1-3 >>> "))
                                if 1 <= shelf_space <= 3:
                                    quantity = int(input("Введите количество для хранения >>> "))
                                    my_reception = my_warehouse.reception(shelf - 1, shelf_space - 1,
                                                                          {"Принтер": my_printer,
                                                                           "Количество": quantity})
                                    if my_reception is True:
                                        print("На склад убранно")
                                        break
                                    elif my_reception is False:
                                        print("Место занято")
                                else:
                                    print("Нет такого места")
                            else:
                                print("Нет такой полки")
                        except ValueError:
                            print("Ошибка ввода!\nПопробуйте её раз!")
                elif choice == 4:
                    break
                else:
                    print("Ошибка ввода!\nПопробуйте её раз!")
    elif choice == "n":
        choice = input("Хотите передать оргтехнику с склад [y/n] >>> ")
        if choice == "y":
            while True:
                try:
                    shelf = int(input("Введите номер полки 1-4 >>> "))
                    if 1 <= shelf <= 4:
                        shelf_space = int(input("Введите место хранения 1-3 >>> "))
                        if 1 <= shelf_space <= 3:
                            company_division = input("Введите подразделение компании >>> ")
                            my_reception = my_warehouse.transfer(shelf - 1, shelf_space - 1, company_division)
                            if my_reception is True:
                                print("Отправлено")
                                break
                            elif my_reception is False:
                                print("На этом месте нечего нет")
                        else:
                            print("Нет такого места")
                    else:
                        print("Нет такой полки")
                except ValueError:
                    print("Ошибка ввода!\nПопробуйте её раз!")
        elif choice == "n":
            break
    else:
        print("Ошибка ввода!")
