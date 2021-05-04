from typing import Callable 
import functools
import logging
import time
import traceback

logger = logging.getLogger()

def repeat(
    _func: Callable =None, 
    *, 
    num_times: int =3, 
    time_sleep: int =5
    ) -> Callable:
    """
    Try repeat the function num_times until success

    Parameters
    ----------
    _func : function, optional
        Wrapped function (arguments allowed), by default None
    num_times : int, optional
        Times to repeat the wrapped function, by default 3
    time_sleep : int, optional
        Seconds to wait between repetitions, by default 5

    Returns
    -------
    function
        Wrapped function
    """    

    """Repeat the function num_times"""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                try:
                    value = func(*args, **kwargs)
                    return value
                except:
                    logger.error(
                        'Error in {function_name}. Trying again in {time_sleep}' 
                        'second(s). Traceback: {error_traceback}'.format(
                            function_name=func.__name__,
                            time_sleep=time_sleep,
                            error_traceback=traceback.format_exc()
                            )
                        )
                    time.sleep(time_sleep)
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)