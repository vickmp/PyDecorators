from typing import Callable
import functools
import logging
import time

logger = logging.getLogger()

def sleep(_func: Callable =None, *, seconds: int =1) -> Callable:
    """
    Sleep given amount of seconds before calling the function

    Parameters
    ----------
    _func : Callable, optional
        Wrapped function (arguments allowed), by default None
    seconds : int, optional
        Seconds to sleep, by default 1

    Returns
    -------
    Callable
        Wrapped function
    """    
    def decorator_sleep_func(func):
        @functools.wraps(func)
        def wrapper_sleep_func(*args, **kwargs):
            time.sleep(seconds)
            value = func(*args, **kwargs)
            return value
        return wrapper_sleep_func
    if _func is None:
        return decorator_sleep_func
    else:
        return decorator_sleep_func(_func)