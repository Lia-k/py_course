# Написать свою реализацию функции reduce
from functools import reduce
from typing import Callable, Union, List, Tuple, Dict, Any


def my_reduce(callback: Callable[[Union[int, float, str],
                                  Union[int, float, str]],
                                 Union[int, float, str]],
              sequence: Union[List, Tuple, Dict]) -> Union[List, Tuple, Dict,
                                                           str, int, float]:
    """
        Works like reduce
    """
    item_reduced = sequence[0]
    for index, value in enumerate(sequence):
        if index == len(sequence) - 1:
            break
        item_reduced = callback(item_reduced, sequence[index + 1])
    return item_reduced
