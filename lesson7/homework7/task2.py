# Написать свою реализацию функции map
from typing import Any, Callable, List, Tuple, Dict, Union


def my_map(callback: Callable,
           sequence: Union[List, Tuple, Dict]) -> List[Any]:
    mapped_list = []
    for item in sequence:
        mapped_item = callback(item)
        mapped_list.append(mapped_item)
    return mapped_list