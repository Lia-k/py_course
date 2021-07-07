# есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"].
# выведите в консоль имена каждое с новой строки выровняв по правой стороне
# используя метод строки и форматирование через f string. Так же над именами
# первой строкой выведини заговловок Names где слово names должно быть
# посредине а остальное пространство заполнено скажем символом "*"
friends_list = [
    "John",
    "Marta",
    "James",
    "Amanda",
    "Marianna"
]
print("Names".center(80, "*"))
for friend in friends_list:
    print(f"{friend.rjust(80, ' ')}")
