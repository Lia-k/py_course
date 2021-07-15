# 2. Написать функцию square, принимающую 1 аргумент — сторону # квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь
# квадрата и диагональ квадрата.
from math import sqrt
from typing import Union


def square(a: Union[int, float]) -> Union[tuple, str]:
    if a > 0:
        square_perimeter = round((4 * a), 2)
        square_area = round((a ** 2), 2)
        square_diagonal = round((a * sqrt(2)), 2)
        return square_perimeter, square_area, square_diagonal
    elif a <= 0:
        return "Please pass a number more than 0"
    else:
        return "Please, pass correct data type "

