from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    unique_values = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in unique_values:
            print("Getting from cache")
        else:
            print("Calculating new result")
            unique_values[args] = func(*args)
        return unique_values[args]
    return inner
