from typing import Any
import datetime

class A:
    def __init__(self,attr):
        self.attr = attr
    
    def __getattribute__(self, attr_name: str) -> Any:
        print("__getattribute__", attr_name)
        return super().__getattribute__(attr_name)
    
    def __getattr__(self, attr_name: str) -> str:
        print("__getattr__", attr_name)
        if attr_name == "current_time":
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            raise AttributeError
        
a=A(42)
print(a.attr)
print(a.myth)
#print(a.not_exist)