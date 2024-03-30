from typing import Callable, Any
import logging

def plus_2(func : Callable[...,Any])-> Callable[...,Any]:
    def wrapper() -> int:
        result=func()
        return result+2
    return wrapper

def get_three() -> int:
    return 3

def get_four() ->int:
    return 4

result1=plus_2(get_three)()
result2=plus_2(get_four)()

logging.basicConfig(level=logging.DEBUG,\
    format='%(asctime)s - %(levelname)s-%(message)s')

logging.info(result1)
logging.info(result2)
