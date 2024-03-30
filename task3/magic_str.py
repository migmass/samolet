class A:
    def __init__(self, x: int) -> None:
        self.x = x
        
    def __str__(self) -> str:
        return f"A({self.x})"

a=A(42)
print(a)
