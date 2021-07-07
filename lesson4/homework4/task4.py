import re

# у вас есть список имен переменных в формате кэмел кейс ["FirstItem",
# "FriendsList", "MyTuple"] преобразовать его в список имен переменных для
# пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]

case_list = [
    "FirstItem",
    "FriendsList",
    "MyTuple"
]
python_list = []
for item in case_list:
    name = re.sub(r"(?=[A-Z])(?!^)", '_', item).lower()
    # ?=[A - Z] - ищет указатель перед любой большой латинской буквой
    # ?!^ - не принимает во внимание начало строки
    python_list.append(name)
print(python_list)
