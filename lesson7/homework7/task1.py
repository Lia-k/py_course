# Написать свою реализацию функции filter.
from typing import Callable, Iterable, List, Any


def my_filter(
        callback: Callable,
        sequence: Iterable[Any]) -> List[Any]:
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
