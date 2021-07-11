# есть строка переданная в качестве квери параметров
# "name=Amanda=sssss&age=32&&salary=1500&currency=quro". Преобразовать эту
# строку в словарь где ключем должно быть значение перед = а значение пары
# значение после равно {name: Amanda......}
parameter = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
fixed_parameter = parameter.strip()
pairs_dict = {}
pairs = fixed_parameter.split("&")
for pair in pairs:
    i = pair.split("=", maxsplit=1)
    if i[0] != '':
        pairs_dict[i[0]] = i[1]
print(pairs_dict)
