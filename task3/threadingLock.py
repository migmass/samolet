from threading import Lock, Thread
from time import sleep

class GlobalState:
    def __init__(self, x: int) -> None:
        self.x = x
        self.lock = Lock()
    def set_x(self, x: int) -> None:
        with self.lock:
            self.x = x
def reader(state: GlobalState) -> None:
    with state.lock:
        if state.x % 2 == 0:
            sleep(0.01) #переключение контекста
            print(f"{state.x=} is even")
        else:
            print(f"{state.x=} is odd")
            
def changer(state: GlobalState) -> None:    
    with state.lock:
        state.set_x(state.x +1)
        
state= GlobalState(2)
t1= Thread(target=reader, args=(state,))
t2= Thread(target=changer, args=(state,)) 
t1.start()
t2.start()
t1.join()
t2.join()   