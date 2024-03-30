from typing import Callable, Any

def multiplier(n:int) -> Callable[...,Any]:
    "multiplier(n) возвращает функцию, умножающую на n"
    
    def mul(k : int) -> int:
        return n*k
    return mul

mul2=multiplier(2) # mul2 -функция, усножающая на 2
print(mul2(5))