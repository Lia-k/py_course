from typing import List
from trainCar import TrainCar


class Train:
    def __init__(self,
                 number_of_locomotives: int,
                 train_number: int,
                 max_speed: int,
                 train_type: str):
        self.__number_of_locomotives = number_of_locomotives
        self.__train_number = train_number
        self.__max_speed = max_speed
        self.__train_type = train_type
        self.__number_of_train_cars: List[object] = []

    @property
    def number_of_locomotives(self):
        return self.__number_of_locomotives

    @property
    def train_number(self):
        return self.__train_number

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def train_type(self):
        return self.__train_type

    @property
    def number_of_train_cars(self):
        return self.__number_of_train_cars

    def __add__(self, other: object):
        return self.__number_of_train_cars.append(other)

    def __len__(self) -> int:
        return len(self.__number_of_train_cars)
