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
