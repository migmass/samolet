import functools
import time
from typing import Callable, Any
import logging

def timer(func: Callable[...,Any])-> Callable[...,Any]:
    @functools.wraps(func)
    def wrapper(*args:Any, **kwargs: Any):
        start = time.perf_counter()
        result = func(*args, **kwargs) # вызывается функция
        runtime = time.perf_counter() - start
        logging.info(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return wrapper

@timer
def complex_calculation():
    """s"""
    time.sleep(0.5)
    return 42

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -\%(levelname)s - %(message)s')

logging.info(complex_calculation())