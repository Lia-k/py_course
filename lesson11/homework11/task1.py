# Описать транспортное средство. Можете брать любое на свое усмотрение. Хочу
# видеть наследование (обычное с несколькими уровнями иерархии), абстракцию,
# сокрытие, инкапсуляцию.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,
                 vehicle_name: str,
                 mover_type: str,
                 environment_movement_type: str
                 ):
        self._vehicle_name = vehicle_name
        self._mover_type = mover_type
        self._environment_movement_type = environment_movement_type
        self._transportation_type = ["people", "goods"]

    @abstractmethod
    def location(self, latitude, longitude):
        """
            Describes moving parameter for the sub-classes
        """
        pass

    @abstractmethod
    def stop(self, parameter):
        """
            Turns off the vehicle engine
        """
        pass

    @abstractmethod
    def break_down(self, parameter):
        """
            Describes breaking parameter for the sub-classes
        """
        pass


class FlyingTransport(Vehicle, ABC):
    def __init__(self, vehicle_name: str,
                 mover_type: str,
                 environment_movement_type: str,
                 transport_model: str,
                 number_of_passengers: int,
                 max_height: int,
                 transport_weight: float,
                 engine_type: str,
                 max_speed: int
                 ):
        super().__init__(vehicle_name, mover_type, environment_movement_type)
        self._transport_model = transport_model
        self._number_of_passengers = number_of_passengers
        self._max_height = max_height
        self._transport_weight = transport_weight
        self._engine_type = engine_type
        self._max_speed = max_speed

    @staticmethod
    def location(latitude: float, longitude: float, **kwargs) -> str:
        """
            Returns the coordinates of the current location
        """
        return f"The coordinates of my location are ({latitude}, {longitude})"

    @staticmethod
    def stop(height: int) -> str:  # pycharm suggests to add **kwargs, but
        # if I do so, I get mypy error
        """
            Turns off engine of the flying vehicle
        """
        if height > 0:
            return "Falling"
        else:
            return "The engine is turned off"

    def fall_down(self, height: int) -> str:
        """
            Counts the number of feet till the ground
        """
        if height > self._max_height:
            return "You could not have gone so high"
        while height > 0:
            height -= 1
            print(f"Falling... {height} feet to the ground")
        return "Oops. You crashed."


class JetPack(FlyingTransport, ABC):
    def __init__(self, vehicle_name: str,
                 mover_type: str,
                 environment_movement_type: str,
                 transport_model: str,
                 number_of_passengers: int,
                 max_height: int,
                 transport_weight: float,
                 engine_type: str,
                 max_speed: int
                 ):
        super().__init__(vehicle_name,
                         mover_type,
                         environment_movement_type,
                         transport_model,
                         number_of_passengers,
                         max_height,
                         transport_weight,
                         engine_type, max_speed)

    def refuel(self, fuel: str) -> str:
        if self._engine_type == "Turbojet engine" and fuel == "hydrogen " \
                                                              "peroxide":
            return "The engine is full"
        else:
            return "Something is wrong. Check the engine type and the fuel."

    def explode(self) -> str:
        return f"Boom! The {self._engine_type} has exploded."

    def break_down(self, broken_part) -> str:
        return f"The {broken_part} is broken."


if __name__ == "__main__":
    jet = JetPack("Jet pack",
                  "Engine",
                  "Flying",
                  "Jet belt",
                  1,
                  3000,
                  200.00,
                  "Turbojet engine",
                  74)
    # Good but I don't see encapsulation of objects -2 points
