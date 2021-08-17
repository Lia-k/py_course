from lesson15.homework15.apple import Apple
from lesson15.homework15.banana import Banana
from lesson15.homework15.cellery import Celery
from lesson15.homework15.strawbarry import Strawberry


class Market:

    def __init__(self, type: str, number_of_sellers: int):
        self._type = type
        self._number_of_sellers = number_of_sellers

    @property
    def type(self):
        return self._type

    @property
    def number_of_sellers(self):
        return self._number_of_sellers

    def increase_sellers(self, additional_sellers: int) -> int:
        self._number_of_sellers = self._number_of_sellers + additional_sellers
        return self._number_of_sellers

    def decrease_sellers(self, decreased_sellers: int) -> int:
        if decreased_sellers <= self._number_of_sellers:
            self._number_of_sellers = self._number_of_sellers - \
                                      decreased_sellers
            return self._number_of_sellers
        else:
            print("Double-check the decreased sellers number")

    @staticmethod
    def get_product(product_name: str):
        if product_name == "apple":
            return Apple()
        if product_name == "banana":
            return Banana()
        if product_name == "celery":
            return Celery()
        if product_name == "strawberry":
            return Strawberry()
        else:
            raise Exception("Incorrect product name.")
