# Создайте функцию которая способна вернуть квадраты четных элементов для
# диапазона от 0 до 1000000000 включительно. Решение должно отрабатывать и
# не фризить ваш комп.

def square_numbers():
    """
        Returns the squares of even numbers in range(0, 1.000.000.000)
        inclusive
    """
    num = 0
    while num <= 1000000000:
        if num % 2 == 0:
            yield num ** 2
        num += 1


gen_func = square_numbers()

# for item in gen_func:
#     print(item)


print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
