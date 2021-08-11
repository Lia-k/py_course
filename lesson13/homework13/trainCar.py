from typing import List, Union


class TrainCar:
    def __init__(self,
                 car_number: int,
                 passengers: List[str, ],
                 sits_in_car: int):
        self.__car_number = car_number
        self.__passengers = passengers
        self.__sits_in_car = sits_in_car

    @property
    def car_number(self):
        return self.__car_number

    @property
    def passengers(self):
        return self.__passengers

    @property
    def sits_in_car(self):
        return self.__sits_in_car

    def add_passengers(self, passenger: str):
        if len(self.__passengers) < self.__sits_in_car:
            return self.__passengers.append(passenger)
        else:
            print("No free sits. Check other car")

    def __len__(self) -> int:
        return len(self.__passengers)

    def __str__(self) -> str:
        return f"[{self.__car_number}]"
