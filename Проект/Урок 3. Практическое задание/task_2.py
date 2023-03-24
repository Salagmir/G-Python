"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def questionnaire(**data):
    a = f"{name} {surname} {year_of_birth} года рождения, проживает в городе {city}," \
        f" email: {email}, телефон: {telephone}"
    return a


name = input("Имя >>> ")
surname = input("Фамилия >>> ")
year_of_birth = input("Год рождения >>> ")
city = input("Город проживания >>> ")
email = input("Email >>> ")
telephone = input("Телефон >>> ")

print(questionnaire(name=name, surname=surname, year_of_birth=year_of_birth, city=city, email=email, telephone=telephone))
