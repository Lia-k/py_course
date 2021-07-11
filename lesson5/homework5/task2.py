# Используя созданный файл в задаче 1 прочитать файл и произвести
# математические операции над каждым элементом. Результат операции вывести в
# консоль. Использовать импорты для импортирования из модуля первой задачи
# нельзя.
import pickle
with open('test/data.txt', "rb") as file:
    file = file.read()
    byte_text = pickle.loads(file)

for item in byte_text:
    if item[2] == 1:
        print(item[0] + item[1])
    elif item[2] == 2:
        print(item[0] - item[1])
    elif item[2] == 3:
        print(item[0] * item[1])
    else:
        print("We are trying to fix this issue. Sorry for inconveniences.")
