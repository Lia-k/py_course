# 3. Написать функцию is_prime, принимающую 1 аргумент — число от 2 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
from typing import Union


def is_prime(a: int) -> Union[bool, str]:
    if a < 2 or a > 1000:
        return "Please, enter a number in range 2-1000 inclusive"
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


if __name__ == '__main__':
    print(is_prime(7))
