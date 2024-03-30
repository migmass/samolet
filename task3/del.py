class A:
    def __new__(cls, x: int) -> 'A':
        print("__new__", cls, x)
        retval=super().__new__(cls)
        print("__new__returned", retval)
        return retval
    
    def __init__(self, x: int) -> None:
        print("__init__", self, x)
        
    def __del__(self) -> None:
        print("__del__", self)
        
a = A(42)