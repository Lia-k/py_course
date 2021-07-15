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
