# У вас есть группа людей с неуникальными именами. Сформируйте список не
# повторяющихся имен (для этой задачи нельзя использовать set. Если в списке
# есть 2 джона нужно взять лишь одного из них. "John Dow", "John Dow",
# "Marta Dow" => "John Dow", "Marta Dow")

people = [
    "John Doe",
    "Marta Doe",
    "Aamir khan",
    "Abhinav Shukla",
    "Abhishek Bachchan",
    "Ajay Devgan",
    "Abhishek Bachchan",
    "Ajay Devgan"
]

# since I can not use set, it looks like I may try to use frozenset.
# They are similar but have difference

unique_people = list(frozenset(people))

# print(unique_people)

# second way in case I was wrong with frozenset

unique_people2 = []

for name in people:
    if name not in unique_people2:
        unique_people2.append(name)

# print(unique_people2)
# Good. Interesting solution but it could be done with dicts
# dict type is able to have only unique keys

# print(list({}.fromkeys(list_of_guests).keys()))
