# 8. Создайте 2 переменные john, marta. Переменные должны быть словарями с ключами: full_name, age, salary, gender, friends, coordinates.
# Требования к структуре:
# Full_name - полное имя
# Age - возраст
# Salary - заработная плата
# Gender - пол человека (используйте булев тип)
# Friends - список друзей из задачи 6 - имеется в виду список из задачи 5?
# Coordinates - долгота и широта из задачи 7
# Вывести в консоль джона и марту ключ и значение: “key => value” где key это ключ пары из словаря а value это значение пары из словаря.
from task1 import john_salary, marta_salary
from task2 import john_age, marta_age
from task3 import john_name, marta_name
from task4 import john_gender, marta_gender
from task5 import john_friends, marta_friends
from task7 import coordinates1

john = {
    "full_name": john_name,
    "age": john_age,
    "salary": john_salary,
    "gender": john_gender,
    "friends": john_friends,
    "coordinates": coordinates1,
}
marta = {
    "full_name": marta_name,
    "age": marta_age,
    "salary": marta_salary,
    "gender": marta_gender,
    "friends": marta_friends,
    "coordinates": coordinates1,
}

for key, value in john.items():
    print(f"{key} => {value}")

for key, value in marta.items():
    print(f"{key} => {value}")

#
# Задача со звездочкой:
# Задача с пункта 8. Вместо строк в списке друзей должны быть такие же словари как джон и марта. Создайте по 2 друга для джона и марты.
# Выведите в консоль поля Джона и Марты.
john_friends1 = {
    "full_name": "Ted",
    "age": 25,
    "salary": 1325.2,
    "gender": True,
    "friends": ["Jes", "Tina", "Mark"],
    "coordinates": (12365.556, 1235.34),
}
john_friends2 = {
    "full_name": "Mark",
    "age": 28,
    "salary": 1562.2,
    "gender": True,
    "friends": ["Jes", "Tina", "Ted"],
    "coordinates": (5684.556, 46485.89),
}
john["friends"] = [john_friends1, john_friends2]

marta_friends1 = {
    "full_name": "Jennifer",
    "age": 20,
    "salary": 956.2,
    "gender": False,
    "friends": ["Tom", "Mina", "Henk"],
    "coordinates": (456841.556, 87986.34),
}
marta_friends2 = {
    "full_name": "Chris",
    "age": 23,
    "salary": 0,
    "gender": True,
    "friends": ["Jes", "Paul", "Peter"],
    "coordinates": (4576411.894, 9658523.561),
}
marta["friends"] = [marta_friends1, marta_friends2]

print(john)
print(marta)
# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
#  Look on how dict is described. It is more preferable view on real projects.
# print(john)
#
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")
