from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args, **kwargs):
        key = (args, kwargs)
        if key in cache_dict:
            print (f"Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print (f"Calculating new result")
            return result
    return wrapper
