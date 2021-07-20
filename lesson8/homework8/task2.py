# Создайте функцию которая способна вернуть квадраты четных элементов для
# диапазона от 0 до 1000000000 включительно. Решение должно отрабатывать и
# не фризить ваш комп.

def square_numbers():
    """
        Returns the squares of even numbers in range(0, 1.000.000.000)
        inclusive
    """
    numbers_generator = (item ** 2
                         for item in range(1000000001)
                         if item % 2 == 0)
    for item in numbers_generator:
        return item
