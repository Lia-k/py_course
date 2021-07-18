# Написать свою реализацию функции map
from typing import Any, Callable, Iterable, List


def my_map(callback: Callable, sequence: Iterable[Any]) -> List[Any]:
    mapped_list = []
    for item in sequence:
        mapped_item = callback(item)
        mapped_list.append(mapped_item)
    return mapped_list
