# 1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними. Если третий
# аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (
# первое на второе). В остальных случаях вернуть строку Not known operation:
# {operation}. Описать функции в приложенном файле таким образом что бы все
# проверки в __main__ блоке task_1 выполнялись корректно. НЕ НУЖНО ВЫЗЫВАТЬ
# ФУНКЦИЮ САМИМ Я ЭТО УЖЕ СДЕЛАЛ В УТВЕРЖДЕНИЯХ "assert"
from typing import Union


def arithmetic(left_operand: Union[int, float],
               right_operand: Union[int, float],
               operation: str) -> Union[int, float, str]:
    """
        Apply arithmetic operation for provided left and right operands
    """
    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    else:
        return f"Not known operation: {operation}"


if __name__ == "__main__":
    assert arithmetic(3, 4, operation="*") == 12
    assert arithmetic(3, 4, operation="+") == 7
    assert arithmetic(25, 5, operation="/") == 5
    assert type(arithmetic(25, 5, operation="/")) == float
    assert arithmetic(5, 5, operation="//") == f"Not known operation: //"
    assert arithmetic.__doc__ == (
        f"\n{' ' * 8}"
        f"Apply arithmetic operation for provided left and right operands\n"
        f"{' ' * 4}"""
    )
    assert arithmetic.__code__.co_name == "arithmetic"
    assert arithmetic.__code__.co_varnames == (
        "left_operand", "right_operand", "operation")
    try:
        arithmetic(1, 2, 3)
    except TypeError as e:
        assert e.__class__ is TypeError
    try:
        arithmetic(left_operand=1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

    try:
        arithmetic(1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

# Excellent
