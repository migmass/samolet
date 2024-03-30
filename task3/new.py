class B:
    pass

class A:
    def __new__(cls):
        return B()
    
a=A()
print(isinstance(a,B))

class MyClass:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self):
        pass