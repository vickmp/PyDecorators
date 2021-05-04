from typing import Callable
import functools
import logging

logger = logging.getLogger()

def debug(_func: Callable =None, *, params: bool =False) -> Callable:
    """
    Print the init and the end of the wrapped function in the logs. 

    Parameters
    ----------
    _func : Callable, optional
        Wrapped function (arguments allowed), by default None
    params : bool, optional
        If True, the attributes received are shown in the logs, 
        by default False

    Returns
    -------
    Callable
        Wrapped function
    """
    def decorator_debug(func):
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            if not params:
                print(f"Init: {func.__name__}")
                logger.debug(f"Init: {func.__name__}")
                value = func(*args, **kwargs)
                logger.debug(f"End: {func.__name__}")
                print(f"End: {func.__name__}")
                return value
            else:
                args_repr = [repr(a) for a in args]                      
                kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
                signature = ", ".join(args_repr + kwargs_repr)  
                print(f"Init: {func.__name__}({signature})")         
                logger.debug(f"Init: {func.__name__}({signature})")
                value = func(*args, **kwargs)
                logger.debug(f"End: {func.__name__!r} returned {value!r}")
                print(f"End: {func.__name__!r} returned {value!r}")         
                return value
        return wrapper_debug
    if _func is None:
        return decorator_debug
    else:
        return decorator_debug(_func)