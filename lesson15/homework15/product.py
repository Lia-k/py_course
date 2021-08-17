from abc import ABC


class Product(ABC):
    _product_name: str = ""

    def __init__(self):
        self.__taste = ''

    @property
    def taste(self):
        return self.__taste
