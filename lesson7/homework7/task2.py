# Написать свою реализацию функции map
from typing import Any, Callable, List, Tuple, Dict, Union


def my_map(callback: Callable[[Union[int, float, str]],
                              Union[int, float, str]],
           sequence: Union[List, Tuple, Dict]) -> List[Any]:
    mapped_list = []
    for item in sequence:
        mapped_item = callback(item)
        mapped_list.append(mapped_item)
    return mapped_list

john = {"name": "John", "age": 23, "gender": "Male"}
james = {"name": "James", "age": 12, "gender": "Male"}
marta = {"name": "Marta", "age": 56, "gender": "Female"}

print(my_map(lambda n: n ** 2, [1, 4, 56, 7, 87]))
print(my_map(lambda n: f"Hello {n}", ["James", "Marta", "John"]))
print(
    my_map(
        lambda man: (man["name"], man["age"]),
        [john, james, marta]
    )
)
