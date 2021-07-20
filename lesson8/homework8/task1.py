# Создать декоратор которые принтит в консоль имя функции которая была
# вызвана. Функция при этом должна работать как и задумывалось. К примеру
# создайте пару функции для арифметических операций суммирования и
# умножения. При вызове этих функций должен возвращаться результат операции
# и предварительно выводиться в консоль имя функции которая была вызвана.
from typing import Union


def func_name(func):
    """
        Returns the name of the function with the function result
    """
    def inner(*args, **kwargs):
        header = func.__name__
        return f"{header}\n{func(*args, **kwargs)}"

    return inner


@func_name
def find_sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
        Returns sum
    """
    return a + b


@func_name
def find_difference(a: Union[int, float],
                    b: Union[int, float]) -> Union[int, float]:
    """
        Returns difference
    """
    return a - b
