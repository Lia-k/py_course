from array import array

# У тебя есть квадраатная матрица 11 * 11 заполненная нулями. Заменить
# диагоняли матрицы единицами.

# for i in range(11):
#     line = ''
#     for j in range(11):
#         if i == j or i + j == 10:
#             line += " 1"
#         else:
#             line += " 0"
#     print(line)

length = 11
matrix = [[0 for _ in range(length)] for row in range(length)]

# for row in range(len(matrix)):
#     for item in range(len(matrix[row])):
#         if row == item or row + item == 10:
#             matrix[row][item] = 1
# print(matrix)

for i in range(length):
    matrix[i][i] = 1
    matrix[i][length - i - 1] = 1
print(matrix)
