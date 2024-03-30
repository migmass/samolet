from typing import Callable, Any
import logging

def plus_2(func : Callable[...,Any])-> Callable[...,Any]:
    def wrapper() -> int:
        result=func()
        return result+2
    return wrapper

@plus_2
def get_three() ->int:
    return 3

@plus_2
def get_four() ->int:
    return 4

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s-%(message)s')

logging.info(get_three())
logging.info(get_four())
