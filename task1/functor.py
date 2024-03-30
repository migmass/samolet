from typing import Callable,Any
import logging

class ToPowerWithDelta(object):
    def __int__ (self, val1:int) ->None:
        self.val1=val1
        self.delta=0
        
    def __call__(self, val2) -> int:
        result = pow(val2, self.val1 + self.delta)
        self.delta +=1
        return result
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -\ %(levelname)s - %(message)s')

to_square=ToPowerWithDelta(2)

logging.info(to_square(7))
logging.info(to_square(7))