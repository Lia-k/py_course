# Написать свою реализацию функции filter.
from typing import Callable, List, Tuple, Dict, Union, Any


def my_filter(
        callback: Callable[[Union[int, float, str]], bool],
        sequence: Union[List, Tuple, Dict]) -> List[Any]:
    """
        Returns a filtered list
    """
    filtered_list = []
    for item in sequence:
        if callback(item):
            filtered_list.append(item)
        else:
            continue
    return filtered_list


john = {"name": "John", "age": 23, "gender": "Male"}
james = {"name": "James", "age": 12, "gender": "Male"}
marta = {"name": "Marta", "age": 56, "gender": "Female"}

print(my_filter(lambda n: n > 5, [1, 4, 56, 7, 87]))
print(my_filter(lambda n: n.startswith('J'), ["James", "Marta", "John"]))
print(
    my_filter(
        lambda man: man["name"].startswith('J'),
        [john, james, marta]
    )
)
